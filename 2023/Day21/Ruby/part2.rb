require "matrix"
require 'set'
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

start = [0, 0]
$x.each_index { |y|
  $x[y].each_index { |x|
    if $x[y][x] == "S"
      start = [y, x]
    end
  }
}

puts start.to_s

$y = $x.map { |y| y.map { Set[] } }
puts $j.to_s

def move(p, m)
  return [p[0] + m[0], p[1] + m[1]]
end
def mod(p)
  y = p[0].modulo($x.length)
  return [y, p[1].modulo($x[y].length)]
end
def div(p)
  m = mod(p)

  y = p[0].div($x.length)
  return [y, p[1].div($x[m[0]].length)]
end
def get(p)
  pp = mod(p)
  return $x[pp[0]][pp[1]]
end

poses = [start]
(0...64).each { |i|
  new_p = {}
  new_p.default = false
  poses.each { |p|
    y, x = p
    if $x[y].nil? or $x[y][x] == "#"
      next
    end
    if y > 0
      new_p[[y - 1, x]] = true
    end
    unless $x[y + 1].nil?
      new_p[[y + 1, x]] = true
    end
    if x > 0
      new_p[[y, x - 1]] = true
    end
    unless $x[y][y + 1].nil?
      new_p[[y, x + 1]] = true
    end
  }

  poses = new_p.each_key.to_a

  poses = poses.filter { |p|
    y, x = p
    not $x[y].nil? and not $x[y][x].nil? and $x[y][x] != "#"
  }

  printf "%d = %d\n", i, poses.length
}

total = poses.length
puts total
File.write(ENV["SOLUTION_FILE"], total.to_s)
