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

start = [0, 0]
$x.each_index { |y|
  $x[y].each_index { |x|
    if $x[y][x] == "S"
      start = [y, x]
    end
  }
}

puts start.to_s

$x.each_index { |y|
  $x[y].each_index { |x|
      printf "%s", $x[y][x]
  }
    printf "\n"
}
  printf "\n"

poses = [start]
(0...64).each { ||
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

  $x.each_index { |y|
    $x[y].each_index { |x|
      if new_p[[y, x]]
        printf "O"
      else
        printf "%s", $x[y][x]
      end
    }
      printf "\n"
  }
    printf "\n"

  poses = new_p.each_key.to_a

  poses = poses.filter { |p|
    y, x = p
    not $x[y].nil? and not $x[y][x].nil? and $x[y][x] != "#"
  }
}

total = poses.length

puts total
File.write(ENV["SOLUTION_FILE"], total.to_s)
