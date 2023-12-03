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

  # printf "\n(%d, %d) -> (%d, %d)\n", lx, ly, rx, ry

  sx = lx
  ex = rx
  sy = ly
  ey = ry

  # unless sy == ey or sx == ex or ((ey - sy) == (ex - sx))
  #   next
  # end
  
  cx = sx
  cy = sy

  # printf "(%d, %d) -> (%d, %d)\n", sx, sy, ex, ey
  while cx != ex or cy != ey
  #   printf "%d != %d || %d != %d\n", cx, ex, cy, ey
    h[cx * 10000 + cy] += 1
    if cx != ex
      cx += cx < ex ? 1 : -1
    end
    if cy != ey
      cy += cy < ey ? 1 : -1
    end
  end
  # printf "%d == %d && %d == %d\n", cx, ex, cy, ey
  h[cx * 10000 + cy] += 1

  total += 1
}

puts h.count { |val| val >= 2 }
