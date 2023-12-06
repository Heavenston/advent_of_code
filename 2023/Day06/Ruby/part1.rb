input = STDIN.read
lines = input.split("\n")

times = lines[0].split(" ")[1..].map { |x| Integer(x.strip) }
distances = lines[1].split(" ")[1..].map { |x| Integer(x.strip) }

puts times.to_s
puts distances.to_s

total = 1
times.each_index { |race|
  i = 0
  (0...times[race]).each { |time|
    if (times[race] - time) * time > distances[race]
      i += 1
    end
  }
  puts i
  total *= i
}
puts total
