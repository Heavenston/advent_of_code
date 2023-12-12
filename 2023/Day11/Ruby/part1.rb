require "matrix"

input = STDIN.read
lines = input.split("\n")

h = {}
h.default = nil


duped1 = []

lines.each { |line|
  if line.include? "#"
    duped1.push(line)
  else
    duped1.push(line)
    duped1.push(line)
  end
}

puts duped1.to_s

duped2 = []
duped1.map { |x| x.chars }.transpose.each { |col|
  duped2.push(col)
  unless col.include? "#"
    duped2.push(col)
  end
}

duped2.transpose.each { |row|
  puts row.join("")
}

final = duped2

galas = []

final.each_index { |x|
  final[x].each_index { |y|
    if final[x][y] == "#"
      galas.push([x, y])
    end
  }
}

total = 0

galas.each_index { |g1|
  galas.each_index { |g2|
    if g1 >= g2
      next
    end

    total += (galas[g1][0] - galas[g2][0]).abs
    total += (galas[g1][1] - galas[g2][1]).abs
  }
}

puts total
File.write(ENV["SOLUTION_FILE"], total.to_s)
