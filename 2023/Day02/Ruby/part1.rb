require "matrix"

input = STDIN.read
lines = input.split("\n")

total = 0
lines.each { |line|
  name, o = line.split(": ")
  id = Integer(name.split(" ")[1])
  cls = o.split("; ").map { |x| x.split(", ").map { |x| x.split " " } }

  # puts cls.map { |x| x.to_s }

  n = {
    "red" => 0,
    "green" => 0,
    "blue" => 0,
  }

  cls.each { |a|
    a.each { |b|
      c, d = b
      n[d] = [n[d], Integer(c)].max
    }
  }
  p = n["red"] * n["green"] * n["blue"]
  total += p
}

puts total
