require "matrix"

input = STDIN.read
lines = input.split("\n")

pos = Vector.zero(2)

dirs = {
  "forward" => Vector[1, 0],
  "down" => Vector[0, 1],
  "up" => Vector[0, -1],
}

lines.each { |line|
  a, b = line.split(" ")
  pos += dirs[a] * Integer(b)
  # puts pos
}

puts pos[0] * pos[1]
