require "matrix"

input = STDIN.read
lines = input.split("\n")

h = Array.new(10000000, 0)

total = 0
lines.each { |line|
  left, right = line.split(" -> ")
  # puts left.to_s
  # puts right.to_s

  lx, ly = left.split(",").map { |x| Integer(x) }
  rx, ry = right.split(",").map { |x| Integer(x) }

  if lx != rx and ry != ly
    next
  end

  sx = [lx, rx].min
  ex = [lx, rx].max
  sy = [ly, ry].min
  ey = [ly, ry].max
  
  # printf "x: %d..%d\n", sx, ex
  # printf "y: %d..%d\n", sy, ey
  (sx..ex).each { |x|
    (sy..ey).each { |y|
      h[x * 10000 + y] += 1
    }
  }

  total += 1
}

puts h.count { |val| val >= 2 }
