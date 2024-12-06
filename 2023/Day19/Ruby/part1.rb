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

def cond(part, c)
  prop = c[:cond][0]
  cond = c[:cond][1]
  val  = Integer(c[:cond][2..])

  if cond == "<"
    return part[prop] < val
  else
    return part[prop] > val
  end
end

def is_acc(part, rates)
  curr = "in"
  until rates[curr].nil?
    rates[curr].each { |c|
      if c[:cond].nil? or cond(part, c)
        curr = c[:dest]
        break
      end
    }
  end
  return curr
end

printf "\n"
printf "\n"

total = 0

p2.each { |p|
  j = is_acc(p, rates)
  printf "%s = %s\n", p.to_s, j
  if j == "A"
    total += p["x"]
    total += p["m"]
    total += p["a"]
    total += p["s"]
  end
}

puts total
File.write(ENV["SOLUTION_FILE"], total.to_s)
