require "matrix"
require "rgl/base"
require "rgl/adjacency"
require "rgl/dot"

input = STDIN.read
lines = input.split("\n")

$x = lines.map { |x| x.chars.map { |j| j } }
$dest = Vector[$x.length - 1, $x[0].length - 1]

$g = RGL::DirectedAdjacencyGraph::new
$g = RGL::AdjacencyGraph::new

$h = {}
$h.default = false

total = 0

rates = {}
s = false
p2 = []

lines.each { |line|
  if line == ""
    s = true
    next
  end
  if not s
    name,rest = line.split("{")
    rates[name] = []
    rest.sub(/\}/, "").split(",").each { |l|
      j = l.split(":")
      if j.length == 1
        rates[name].push({
          cond: nil,
          dest: l.split(":")[0]
        })
      elsif
        rates[name].push({
          cond: l.split(":")[0],
          dest: l.split(":")[1]
        })
      end
    }
  else
    h = {}
    line.gsub(/{|}/, "").split(",")
      .map { |x| x.split("=") }
      .each { |x| h[x[0]] = Integer(x[1]) }
    p2.push(h)
  end
}

puts rates.to_s
puts p2.to_s

printf "\n"
printf "\n"

total = 0

rejes = []
acces = []
todo = [[{
  "x" => [0, 4001],
  "m" => [0, 4001],
  "a" => [0, 4001],
  "s" => [0, 4001],
}, "in"]]

while todo.length > 0
  ranges, name = todo.pop
  curr = rates[name]

  printf "%s %s\n", ranges.to_s, name.to_s
  printf " > %s\n", curr.to_s

  curr.each { |c|
    in_ = ranges.clone
    in_.each_key { |k| in_[k] = in_[k].clone }
    out_ = ranges.clone
    out_.each_key { |k| out_[k] = out_[k].clone }

    unless c[:cond].nil?
      prop = c[:cond][0]
      cond = c[:cond][1]
      val  = Integer(c[:cond][2..])

      if cond == "<"
        if in_[prop][1] > val
          in_[prop][1] = val
        end
        if in_[prop][0] > val
          in_[prop][0] = val
        end

      if out_[prop][1] < val
        out_[prop][1] = val
      end
      if out_[prop][0] < val
        out_[prop][0] = val
      end
      elsif cond == ">"
        if in_[prop][0] < val
          in_[prop][0] = val
        end
        if in_[prop][1] < val
          in_[prop][1] = val
        end

        if out_[prop][1] > val
          out_[prop][1] = val
        end
        if out_[prop][0] > val
          out_[prop][0] = val
        end
      end
    end

    if c[:dest] == "A"
      acces.push(in_)
    elsif c[:dest] == "R"
      rejes.push(in_)
    else
      todo.push([in_, c[:dest]])
    end

    ranges = out_
  }

  printf " > %s %s\n", ranges.to_s, name.to_s
  printf "\n"
end

def sizeof(me)
  t = 1
  me.each_value { |m|
    t *= m[1] - m[0] - 1
  }
  return t
end

total = 1

acces.each { |me|
  total += sizeof(me)
}

puts total
File.write(ENV["SOLUTION_FILE"], total.to_s)
