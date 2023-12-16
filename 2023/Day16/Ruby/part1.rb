require "matrix"

input = STDIN.read
lines = input.split("\n")

h = {}
h.default = false

x = lines.map { |l| l.chars }

total = 0

bs = {
  [Vector[0, 0], Vector[0, 1]] => 1,
}
bs.default = 0
printf "%s\n", bs.to_s

do_ = true
while bs.length > 0
  do_ = false

  new_bs = {}
  new_bs.default = 0

  bs.each.filter { |k, v| v > 0 }.map { |k, v| k }.each { |b|
    pos, dir = b

    unless pos[0] >= 0 and pos[0] < x.length and pos[1] >= 0 and pos[1] < x[pos[0]].length
      next
    end

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
  printf "%s\n", bs.length
  puts h.count { |k, v| v == true }
end

total = h.count { |k, v| v == true }
puts total
File.write(ENV["SOLUTION_FILE"], total.to_s)
