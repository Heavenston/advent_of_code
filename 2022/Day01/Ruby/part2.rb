input = STDIN.read

lines = input.split("\n")

sol = lines.chunk_while { |a, b| b != "" }
  .map { |x| x.filter { |x| x != "" }.map { |x| Integer(x) }.sum }
  .max(3)
  .sum
puts sol

# i = 0
# x.each { |line|
#   i += 1
#   printf "%d: %s\n", i, line
# }
