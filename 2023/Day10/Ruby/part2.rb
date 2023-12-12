require "matrix"

input = STDIN.read
lines = input.split("\n")

h = {}
h.default = nil

total = 0

pas = lines.map { |line| line.chars }

dists = {}
dists.default = 9999999999999

def is_val(pas, pos)
  if pos[0] < 0 or pos[0] >= pas.length
    return false
  end
  if pos[1] < 0 or pos[1] >= pas[pos[0]].length
    return false
  end
  return true
end

def fil_val(pas, poses)
  poses.filter { |x| is_val(pas, x) }
end

cons = {}
pas.each_index { |row|
  pas[row].each_index { |col|
    pos = [row, col]
    j = pas[row][col]
    cons[pos] = []
    if j == "S"
      dists[pos] = 0
    elsif j == "|"
      cons[pos] = fil_val(pas, [[row + 1, col], [row - 1, col]])
    elsif j == "-"
      cons[pos] = fil_val(pas, [[row, col - 1], [row, col + 1]])
    elsif j == "L"
      cons[pos] = fil_val(pas, [[row - 1, col], [row, col + 1]])
    elsif j == "F"
      cons[pos] = fil_val(pas, [[row + 1, col], [row, col + 1]])
    elsif j == "7"
      cons[pos] = fil_val(pas, [[row + 1, col], [row, col - 1]])
    elsif j == "J"
      cons[pos] = fil_val(pas, [[row - 1, col], [row, col - 1]])
    end
  }
}

pas.each_index { |row|
  pas[row].each_index { |col|
    pos = [row, col]
    j = pas[row][col]
    connected = {}
    connected.default = false
    (-1..1).each { |dr|
      (-1..1).each { |dc|
        r = row + dr
        c = col + dc
        pos2 = [r, c]
        if not is_val(pas, pos2)
          next
        end

        if cons[pos2].any? { |x| x[0] == row and x[1] == col }
          connected[pos2] = true
        end
      }
    }
    if j == "S"
      cons[pos] = connected.each_key.map{|x|x }
    else
      cons[pos] = cons[pos].filter { |p| connected[p] }
    end
  }
}

puts cons.to_s

imps = []
pas.each_index { |row|
  pas[row].each_index { |col|
    if pas[row][col] == "."
      next
    end
    imps.push([row, col])
  }
}

ups = imps.clone

do_ = 1
while do_ > 0
  do_ = 0
  new_ups = []
  ups.each { |pos|
    m = dists[pos]
    cons[pos].each { |pos2|
      if dists[pos2] + 1 < m
        m = dists[pos2] + 1
      end
    }
    if m != dists[pos]
      do_ += 1
      dists[pos] = m
      new_ups.push(*cons[pos])
    end
  }
  ups = new_ups
end

is_loop = {}
is_loop.default = false
pas.each_index { |row|
  pas[row].each_index { |col|
    pos = [row, col]
    if dists[pos] == dists.default 
      is_loop[pos] = false
    else
      is_loop[pos] = true
    end
  }
}

pas.each_index { |row|
  pas[row].each_index { |col|
    pos = [row, col]
    if is_loop[pos]
      printf "Y"
    else
      printf "N"
    end
  }
  printf "\n"
}

puts dists.to_s
total = dists.each_value.max

puts total
File.write(ENV["SOLUTION_FILE"], total.to_s)
