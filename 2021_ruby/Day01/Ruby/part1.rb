input = STDIN.read
lines = input.split("\n").map { |x| Integer(x) }

total = 0
p = lines[0]
lines[1..].each { |line|
  if line > p
    total += 1
  end
  p = line
}
puts total
