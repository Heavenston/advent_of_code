require "matrix"
require "rgl/base"
require "rgl/adjacency"
require "rgl/dot"

input = STDIN.read
lines = input.split("\n")

$x = lines.map { |x| x.chars.map { |j| j } }
$dest = Vector[$x.length - 1, $x[0].length - 1]

$g = RGL::DirectedAdjacencyGraph::new
# $g = RGL::AdjacencyGraph::new

$h = {}
$h.default = false

def get(p)
  return $x[p[0]][p[1]]
end

def is_in(p)
  (not (p[1] < 0 or p[0] < 0 or p[0] >= $x.length or p[1] >= $x[p[0]].length))
end

def man_dist(a, b)
  (a[0] - b[0]).abs + (a[1] - b[1]).abs
end

def dbg(x)
  puts x.to_s
end

$x.each_index { |y|
  $x[y].each_index { |x|
    p = Vector[y, x]
    cc = get(p)
    dd = [
      (cc == "." or cc == ">") ? Vector[0, 1] : nil,
      (cc == "." or cc == "<") ? Vector[0, -1] : nil,
      (cc == "." or cc == "v") ? Vector[1, 0] : nil,
      (cc == "." or cc == "^") ? Vector[-1, 0] : nil
    ]
    .filter { |x| not x.nil? } .map { |x| x + p }
    .filter{ |x| is_in(x) }
    .filter{ |x| get(x) != "#" }
    .each { |np|
      $g.add_edge(p, np)
    }
  }
}

# puts $g.topsort_iterator.to_a

total = 0

paths = [[Vector[0, 1]]]

$end = Vector[$x.length - 1, $x[0].length - 2]
founds = []

while paths.length > 0
  best, i = paths.each_with_index.min_by { |x, i| -(man_dist(x.last, $end) + x.length) }
  # best, i = paths.each_with_index.min_by { |x, i| x.length }
  paths.delete_at(i)
  # puts best.to_s

  if best.include?($end)
    puts best.length - 1
    founds.push(best)
    next
  end

  pos = best.last
  cc = get(pos)

  [
    (cc == "." or cc == ">") ? Vector[0, 1] : nil,
    (cc == "." or cc == "<") ? Vector[0, -1] : nil,
    (cc == "." or cc == "v") ? Vector[1, 0] : nil,
    (cc == "." or cc == "^") ? Vector[-1, 0] : nil
  ].filter { |x| not x.nil? }.each { |dp|
    np = pos + dp
    if best.include?(np)
      next
    end
    unless is_in(np)
      next
    end
    if get(np) == "#"
      next
    end
    new = best.clone()
    new.push(np)
    paths.push(new)
  }
end

best_path = founds.max_by { |x| x.length }
total = best_path.length - 1

if best_path.nil?
  printf "not found\n"
  exit()
end

# $x.each_index { |y|
#   $x[y].each_index { |x|
#     p = Vector[y, x]
#     if best_path.include?(p) and get(p) == "."
#       printf "O"
#     else
#       printf "%s", get(p)
#     end
#   }
#   printf "\n"
# }
# printf "\n"

puts total
File.write(ENV["SOLUTION_FILE"], total.to_s)
