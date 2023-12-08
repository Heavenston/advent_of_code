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

currs = poses.each_key.filter { |q| q.chars.last == "A" }
times = Array.new(currs.length, 0)

puts currs.to_s
until currs.all? { |q| q.chars.last == "Z" }
  ints.each { |p|
    i = (p == "R" ? 1 : 0)
    currs.each_index { |ci| 
      if currs[ci].chars.last == "Z" then next end
      times[ci] += 1
      currs[ci] = poses[currs[ci]][i]
      # printf "%s[%s] = %s\n", currs[ci], i, poses[currs[ci]][i]
    }
    # puts currs.to_s
  }
end

puts times.reduce(:lcm)
