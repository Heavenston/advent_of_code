input = STDIN.read
lines = input.split("\n")

total = 0
lines.each { |line|
  printf "%d: %s\n", total, line
  total += 1
}
puts total
