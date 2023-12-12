require "matrix"

input = STDIN.read
lines = input.split("\n")

galas = []

puts "looking for galas"

lines.each_index { |y|
  lines[y].chars.each_index { |x|
    if lines[y][x] == "#"
      galas.push([x, y])
    end
  }
}

galas_moved = galas.map { |x| x.clone }
puts "found galas"

h = {}
h.default = nil

exp = 1_000_000 - 1

lines.each_index { |y|
  line = lines[y]
  unless line.include? "#"
    puts y, line
    galas.each_index { |g1|
      if galas[g1][1] > y
        galas_moved[g1][1] += exp
      end
    }
  end
}

puts galas.to_s
puts galas_moved.to_s

puts "a"

lines.map { |x| x.chars }.transpose.each_with_index { |col, x|
  unless col.include? "#"
    galas.each_index { |g1|
      if galas[g1][0] > x
        galas_moved[g1][0] += exp
      end
    }
  end
}

puts galas.to_s
puts galas_moved.to_s

puts "b"

total = 0

galas_moved.each_index { |g1|
  galas_moved.each_index { |g2|
    if g1 >= g2
      next
    end

    total += (galas_moved[g1][0] - galas_moved[g2][0]).abs
    total += (galas_moved[g1][1] - galas_moved[g2][1]).abs
  }
}

puts total
File.write(ENV["SOLUTION_FILE"], total.to_s)
