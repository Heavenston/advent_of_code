require "matrix"
require "rgl/base"
require "rgl/adjacency"
require "rgl/dot"

input = STDIN.read
lines = input.split("\n")

def deep(x)
  return Marshal.load(Marshal.dump(x))
end

def deep_eq(a, b)
  return Marshal.dump(a) == Marshal.dump(b)
end

$x = lines.map { |x| x.chars.map { |j| j } }
$dest = Vector[$x.length - 1, $x[0].length - 1]

$g = RGL::DirectedAdjacencyGraph::new
$g = RGL::AdjacencyGraph::new

$h = {}
$h.default = nil

total = 0

lines.each { |line|
  left, rigth = line.split(" -> ")

  l = {}

  if left[0] == "&"
    l[:name] = left[1..]
    l[:type] = :conj
  elsif left[0] == "%"
    l[:name] = left[1..]
    l[:type] = :flip
  else
    l[:name] = left
    l[:type] = :broad
  end

  l[:dests] = rigth.split(", ")

  $h[l[:name]] = l

}

puts $h.to_s

$states_flip = {}
$states_conj = {}
$h.each_value { |mod|
  if mod[:type] == :flip
    $states_flip[mod[:name]] = false
  elsif mod[:type] == :conj
    if $states_conj[mod[:name]].nil?
    $states_conj[mod[:name]] = {}
    end
    $states_conj[mod[:name]].default = 0
  end

  mod[:dests].each { |d|
    if $states_conj[d] == nil
      $states_conj[d] = {}
    end
    $states_conj[d][mod[:name]] = 0
  }
}

def proc_pulse(source, mod, pulse)
  name = mod[:name]

  out = nil

  if mod[:type] == :flip and pulse == 0
    $states_flip[name] = (not ($states_flip[name]))

    if $states_flip[name]
      out = 1
    else
      out = 0
    end
  elsif mod[:type] == :conj
    $states_conj[name][source] = pulse
    if $states_conj[name].each_value.all? { |x| x == 1 }
      out = 0
    else
      out = 1
    end
  elsif mod[:type] == :broad
    out = pulse
  end

  unless out.nil?
    h = []

    mod[:dests].each { |d|
      h.push([name, d, out])
    }

    return h
  end

  return []
end

$cycles = {}

# total = [0, 0]

$iters = 1_000_000

puts "A"

(1..$iters).each {
  pulses = [["button", "broadcaster", 0]]
  while pulses.length > 0
    source, dest, pulse = pulses.shift

    # printf "%s -%s> %s\n", source, if pulse == 0 then "low" else "high" end, dest

    unless $h[dest].nil?
      pulses.push(*proc_pulse(source, $h[dest], pulse))
    end
    # puts pulses.to_s
  end

  $h.each { |key, val|
    if $cycles[key].nil?
      $cycles[key] = []
    end
    $cycles[key].push(deep([
      $states_flip[key],
      $states_conj[key]
    ]))
  }
  # printf "\n\n"
}

puts "B"

(1...$iters).each { |cycle_size|
# [3].each { |cycle_size|
  $cycles.each_value.all? { |x|
    y = x.each_slice(cycle_size).to_a
    a = y[0]
    if y.all? { |z| z == a }
      printf "FOUND"
    end
  }
}

puts total
File.write(ENV["SOLUTION_FILE"], total.to_s)
