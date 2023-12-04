input = STDIN.read
lines = input.split("\n")

total = 0
lines.each { |line|
  # printf "%d: %s\n", total, line

  id = Integer(line.split(": ")[0].split(" ")[1])
  win, mine = line.split(": ")[1].split(" | ").map{ |s| s.split(" ").map { |x| Integer(x) } }

  # puts id, win, mine

  val = 0

  win.each { |w|
    in_ = mine.any? { |m| w == m }
    if in_
      if val == 0
        val = 1
      else
        val *= 2
      end
    end
  }

  # puts val
  total += val
}
puts total
