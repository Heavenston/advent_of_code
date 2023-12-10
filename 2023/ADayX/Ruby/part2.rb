require "matrix"

input = STDIN.read
lines = input.split("\n")

h = {}
h.default = nil

total = 0

lines.each { |line|
  printf "%d: %s\n", total, line
  total += 1
}

puts total
File.write(ENV["SOLUTION_FILE"], total.to_s)
