input = STDIN.read
lines = input.split("\n")

ints = lines[0].chars

poses = {}

total = 0
lines[2..].each { |line|
  name, dirs = line.split(" = ")

  poses[name] = dirs.gsub(/\(|\)/, "").split(", ")
}

puts poses.to_s

curr = "AAA"

j = 0
while curr != "ZZZ"
  ints.each { |p|
    j += 1
    i = p == "R" ? 1 : 0
    printf "%s[%s] = %s\n", curr, i, poses[curr][i]
    curr = poses[curr][i]
  }
end

puts j
