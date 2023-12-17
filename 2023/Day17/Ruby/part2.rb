require "matrix"
require "rgl/base"
require "rgl/adjacency"
require "rgl/dot"

input = STDIN.read
lines = input.split("\n")

$x = lines.map { |x| x.chars.map { |j| Integer(j) } }
$dest = Vector[$x.length - 1, $x[0].length - 1]

g = RGL::DirectedAdjacencyGraph::new
g = RGL::AdjacencyGraph::new

h = {}
h.default = nil

total = 0

def in?(x)
  x[0] >= 0 and x[0] < $x.length and x[1] >= 0 and x[1] < $x[x[0]].length
end

def continue(p)
  left = nil
  rigth = nil
  if p[:dir] == Vector[0, 1]
    left = Vector[-1, 0]
    rigth = Vector[1, 0]
  elsif p[:dir] == Vector[0, -1]
    left = Vector[1, 0]
    rigth = Vector[-1, 0]
  elsif p[:dir] == Vector[1, 0]
    left = Vector[0, 1]
    rigth = Vector[0, -1]
  elsif p[:dir] == Vector[-1, 0]
    left = Vector[0, -1]
    rigth = Vector[0, 1]
  end

  left_p = p[:pos] + left
  rigth_p = p[:pos] + rigth
  for_p = p[:pos] + p[:dir]

  new = []

  if p[:tur] < 10 and in?(for_p)
    new.push({
      "loss": p[:loss] + $x[for_p[0]][for_p[1]],
      "pos": for_p,
      "dir": p[:dir],
      "tur": p[:tur] + 1
    })
  end
  if p[:tur] >= 3 and in?(left_p)
    new.push({
      "loss": p[:loss] + $x[left_p[0]][left_p[1]],
      "pos": left_p,
      "dir": left,
      "tur": 0
    })
  end
  if p[:tur] >= 3 and in?(rigth_p)
    new.push({
      "loss": p[:loss] + $x[rigth_p[0]][rigth_p[1]],
      "pos": rigth_p,
      "dir": rigth,
      "tur": 0
    })
  end

  return new
end

def dist(a, b)
  r = a - b
  return r[0].abs + r[1].abs
end

finished = { }

curr = { }
curr.default = false

bests = {}

curr[{"loss": 0, "pos": Vector[0,0], "dir": Vector[0,1], "tur": 0}] = true

found = false
while curr.length > 0 and not found
  best = curr.each_key.min_by { |x| x[:loss] }
  curr.delete(best)

  continue(best).each { |n|
    bestt = bests[[n[:pos], n[:tur], n[:dir]]]
    if not bestt.nil? and n[:loss] >= bestt
      next
    end
    bests[[n[:pos], n[:tur], n[:dir]]] = n[:loss]
    curr[n] = true
  }

  puts best.to_s

  f = curr.each_key
    .filter { |x| x[:pos] == $dest and x[:tur] >= 4 }
    .to_a

  f.each { |f|
    finished[f] = true
    curr.delete(f)
    found = true
  }
  # found = curr
  #   .each_key
  #   .any? { |x| x[:pos] == $dest and x[:tur] >= 4 }
end

puts finished.to_s
total = finished.each_key
  .filter { |x| x[:pos] == $dest and x[:tur] >= 4 }
  .map { |x| x[:loss] }.min

puts total
File.write(ENV["SOLUTION_FILE"], total.to_s)
