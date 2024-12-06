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

$dirs = {
  0 => Vector[1, 0],
  3 => Vector[0, 1],
  1 => Vector[0, -1],
  2 => Vector[-1, 0],
}

area = 0
perim = 0

pos = Vector[0, 0]
lines.each { |line|
  _a, _b, h = line.split(" ")

  n = Integer(h[2..6], 16)
  dir = $dirs[Integer(h[-2])]

  pos += dir * n
}

total = area + perim

# puts "step 1 finished"

# min_x = $h.each_key.map { |x| x[0] }.min - 1
# max_x = $h.each_key.map { |x| x[0] }.max + 1
# min_y = $h.each_key.map { |x| x[1] }.min - 1
# max_y = $h.each_key.map { |x| x[1] }.max + 1

# $in = {}
# $in.default = true

# (min_x..max_x).each { |x|
#   $in[Vector[x, min_y]] = false
#   $in[Vector[x, max_y]] = false
# }
# (min_y..max_y).each { |y|
#   $in[Vector[min_x, y]] = false
#   $in[Vector[max_x, y]] = false
# }

# todo = $in.each_key.to_a

# do_ = true
# while todo.length > 0
#   do_ = false

#   ntodo = []
#   todo.each { |k|
#     if $h[k]
#       next
#     end
#     (-1..1).each { |dx|
#       (-1..1).each { |dy|
#         np = k + Vector[dx, dy]
#         if np[0] < min_x or np[0] > max_x or np[1] < min_y or np[1] > max_y
#           next
#         end
#         if $in[np]
#           ntodo.push(np)
#           $in[np] = false
#         end
#       }
#     }
#   }
#   todo = ntodo

#   # (min_x..max_x).each { |x|
#   #   (min_y..max_y).each { |y|
#   #     if $h[Vector[x, y]]
#   #       next
#   #     end

#   #     any_not_in = false
#   #     if any_not_in and $in[Vector[x, y]]
#   #       do_ = true
#   #       $in[Vector[x, y]] = false
#   #     end
#   #   }
#   # }

#   (min_y..max_y).each { |y|
#     (min_x..max_x).each { |x|
#       if $in[Vector[x, y]]
#         printf "#"
#       else
#         printf "."
#       end
#     }
#     printf "\n"
#   }
#   printf "\n"
# end

# total = 0

# (min_y..max_y).each { |y|
#   (min_x..max_x).each { |x|
#     if $in[Vector[x, y]] or $h[Vector[x, y]]
#       total += 1
#       printf "#"
#     else
#       printf "."
#     end
#   }
#   printf "\n"
# }
# printf "\n"

puts total
File.write(ENV["SOLUTION_FILE"], total.to_s)
