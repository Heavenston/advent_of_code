input = STDIN.read
lines = input.split("\n")

times = Integer(lines[0].split(" ")[1..].map { |x| x.strip }.join(""))
distances = Integer(lines[1].split(" ")[1..].map { |x| x.strip }.join(""))

puts times.to_s
puts distances.to_s

total = 1
i = 0
(0...times).each { |time|
  if (times - time) * time > distances[race]
    i += 1
  end
}
puts i
total *= i
puts total
