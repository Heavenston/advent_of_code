require "matrix"

input = STDIN.read
lines = input.split("\n")

$x = lines.map { |l| l.chars }

def compute(bs)
  dont_redo = {}
  dont_redo.default = false
  x = $x

  bs.default = 0

  h = {}
  h.default = false

  not_moved = 0
  total = 0

  while not_moved < 10
    new_bs = {}
    new_bs.default = 0

    bs.each.filter { |k, v| v > 0 }.map { |k, v| k }.each { |b|
      pos, dir = b

      if dont_redo[[pos, dir]]
        next
      end
      unless pos[0] >= 0 and pos[0] < x.length and pos[1] >= 0 and pos[1] < x[pos[0]].length
        next
      end
      dont_redo[[pos, dir]] = true

      h[pos.clone] = true

      new_pos = pos.clone
      new_dir = dir.clone

      # printf "(%d, %d) = %s\n", pos[0], pos[1], x[pos[0]][pos[1]]

      if x[pos[0]][pos[1]] == "."
        new_bs[[new_pos + new_dir, new_dir]] += 1
      elsif x[pos[0]][pos[1]] == "/"
        if dir[0] == 0 and dir[1] == 1
          new_dir[0] = -1
          new_dir[1] = 0
        elsif dir[0] == 0 and dir[1] == -1
          new_dir[0] = 1
          new_dir[1] = 0
        elsif dir[0] == 1 and dir[1] == 0
          new_dir[0] = 0
          new_dir[1] = -1
        elsif dir[0] == -1 and dir[1] == 0
          new_dir[0] = 0
          new_dir[1] = 1
        else
          puts "panic"
        end

        new_bs[[new_pos + new_dir, new_dir]] += 1
      elsif x[pos[0]][pos[1]] == "\\"
        if dir[0] == 0 and dir[1] == 1
          new_dir[0] = 1
          new_dir[1] = 0
        elsif dir[0] == 0 and dir[1] == -1
          new_dir[0] = -1
          new_dir[1] = 0
        elsif dir[0] == 1 and dir[1] == 0
          new_dir[0] = 0
          new_dir[1] = 1
        elsif dir[0] == -1 and dir[1] == 0
          new_dir[0] = 0
          new_dir[1] = -1
        else
          puts "panic"
        end

        new_bs[[new_pos + new_dir, new_dir]] += 1
      elsif x[pos[0]][pos[1]] == "-"
        # not pointy end
        if dir[0] != 0
          new_bs[[new_pos + Vector[0, -1], Vector[0, -1]]] += 1
          new_bs[[new_pos + Vector[0, 1], Vector[0, 1]]] += 1
        else
          new_bs[[new_pos + new_dir, new_dir]] += 1
        end
      elsif x[pos[0]][pos[1]] == "|"
        # not pointy end
        if dir[1] != 0
          new_bs[[new_pos + Vector[-1, 0], Vector[-1, 0]]] += 1
          new_bs[[new_pos + Vector[1, 0], Vector[1, 0]]] += 1
        else
          new_bs[[new_pos + new_dir, new_dir]] += 1
        end
      else
        puts "panic"
      end
    }

    bs = new_bs
    new_count = h.count { |k, v| v == true }
    # printf "bs: %s\n", bs.length
    # printf "h:  %s\n", new_count
    if total == new_count
      not_moved += 1
    else
      not_moved = 0
    end
    total = h.count { |k, v| v == true }
  end

  return total
end

dirs = {  }
dirs.default = nil

(0...$x.length).each { |y|
  dirs[[Vector[y, 0], Vector[0, 1]]] = 0
  dirs[[Vector[y, $x[y].length - 1], Vector[0, -1]]] = 0
}

(0...$x[0].length).each { |x|
  dirs[[Vector[0, x], Vector[1, 0]]] = 0
  dirs[[Vector[$x.length - 1, x], Vector[-1, 0]]] = 0
}

printf "dirs to do: %d\n", dirs.length
index = 0
dirs.each { |k, v|
  printf "%d / %d = ", index, dirs.length
  dirs[k] = compute({ k => 1 })
  printf "%d\n", dirs[k]
  index += 1
}

total = dirs.each_value.max
# total = compute({ [Vector[0, 0], Vector[0, 1]] => 1 })
puts total
File.write(ENV["SOLUTION_FILE"], total.to_s)
