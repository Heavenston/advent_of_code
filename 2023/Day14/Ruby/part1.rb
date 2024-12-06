require "matrix"

input = STDIN.read
lines = input.split("\n")

k = lines.map { |x| x.chars }

h = {}
h.default = nil

total = 0

do_ = true
while do_
  new = k.map { |x| x.map { "." } }

  do_ = false
  k.each_index { |y|
    k[y].each_index { |x|
      c = k[y][x]
      if c == "O"
        if y == 0 or k[y - 1][x] != "."
          new[y][x] = "O"
          next
        end
        do_ = true
        new[y - 1][x] = "O"
      else
        new[y][x] = k[y][x]
      end
    }
  }

  k = new
end

total = 0

k.each { |x|
  printf "%s\n", x.join("")
}
printf "\n"

# cols = (0...k[0].length).to_a
# i = 0
# while cols.length != 0
#   keep = {}
#   keep.default = false

#   cols.each { |col|
#     printf "%s", k[i][col]
#     if k[i][col] == "O"
#       printf "(%d)", k.length - i
#       total += k.length - i
#       keep[col] = true
#     end
#   }
#   printf "\n"

#   cols = cols.filter { |c| keep[c] }

#   i += 1
# end

k.each_index { |i|
  k[i].each { |c|
    if c == "O"
      total += k.length - i
    end
  }
}

puts total
File.write(ENV["SOLUTION_FILE"], total.to_s)
