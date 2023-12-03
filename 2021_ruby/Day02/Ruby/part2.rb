require "matrix"

input = STDIN.read
lines = input.split("\n")

aim = 0
pos = Vector.zero(2)

dirs = {
  "forward" => Vector[1, 0],
  "down" => Vector[0, 1],
  "up" => Vector[0, -1],
}

lines.each { |line|
  a, b = line.split(" ")
  b = Integer(b)
  if a == "forward" then
    pos[0] += b
    pos[1] += aim * b
  elsif a == "down"
    aim += b
  elsif a == "up"
    aim -= b
  end
  # puts pos
}

puts pos[0] * pos[1]
