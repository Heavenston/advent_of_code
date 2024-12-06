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

lines.each { |line|
  printf "%d: %s\n", total, line
  total += 1
}

puts total
File.write(ENV["SOLUTION_FILE"], total.to_s)
