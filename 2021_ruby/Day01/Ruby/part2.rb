input = STDIN.read
lines = input.split("\n").map { |x| Integer(x) }

w = (0..lines.size - 3).map { |x| lines[x, 3].sum }

total = 0
p = w[0]
w[1..].each { |line|
  if line > p
    total += 1
  end
  p = line
}
puts total
