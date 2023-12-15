require "matrix"

input = STDIN.read
lines = input.split("\n")

total = 0

total = lines[0].split(",").map { |l|
  s = 0
  l.chars.each { |x| 
    s += x.ord
    s = (s * 17) % 256
  }
  puts s
  s
}.sum

puts total
File.write(ENV["SOLUTION_FILE"], total.to_s)
