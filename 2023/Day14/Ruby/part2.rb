require "matrix"

input = STDIN.read
lines = input.split("\n")

k = lines.map { |x| x.chars }

h = {}
h.default = nil

total = 0

def cclone(k)
  k.map { |x| x.clone }
end

def pr(k)
  k.each { |r|
    printf "%s\n", r.join("")
  }
  printf "\n"
end

def move(k, dx, dy)
  do_ = true
  # pr(k)
  while do_
    new = k.map { |x| x.map { "." } }

    do_ = false
    k.each_index { |y|
      k[y].each_index { |x|
        c = k[y][x]
        if c == "O"
          nx = x + dx
          ny = y + dy
          if ny < 0 or nx < 0 or ny >= k.length or nx >= k[ny].length or k[ny][nx] != "."
            new[y][x] = "O"
          else
            # printf "(%d, %d) -> (%d, %d)\n", x, y, nx,ny
            do_ = true
            new[ny][nx] = "O"
          end
        elsif c == "#"
          new[y][x] = c
        end
      }
    }

    k = new
  end

  return k
end

$cycle_h = {}

def cycle(k)
  if $cycle_h[k] != nil
    return nil
    return $cycle_h[k]
  end
  o = k
  k = move(k, 0, -1)
  k = move(k, 1, 0)
  k = move(k, 0, 1)
  k = move(k, -1, 0)
  $cycle_h[o] = k
  return k
end

def score(k)
  s = 0
  k.each_index { |i|
    k[i].each { |c|
      if c == "O"
        s += k.length - i
      end
    }
  }
  return s
end

(0...1000000000).each { |i|
  k = cycle(k)
  if k == nil
    break
  end
  printf "score: (%d) = %d\n", i, score(k)
}

total = 0

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


puts total
File.write(ENV["SOLUTION_FILE"], total.to_s)
