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

  sx = [lx, rx].min
  ex = [lx, rx].max
  sy = [ly, ry].min
  ey = [ly, ry].max

  # unless lx == ly or rx == ry or ((lx - rx) == (ly - ry))
  #   next
  # end
  unless sy == ey or sx == ex or ((ey - sy) == (ex - sx))
    next
  end
  
  cx = sx
  cy = sy

  # printf "\n(%d, %d) -> (%d, %d)\n", sx, sy, ex, ey
  while cx < ex or cy < ey
  #   printf "%d < %d and %d < %d\n", cx, ex, cy, ey
    h[cx * 10000 + cy] += 1
    if cx < ex
      cx += 1
    end
    if cy < ey
      cy += 1
    end
  end
  # printf "%d < %d and %d < %d\n", cx, ex, cy, ey
  h[cx * 10000 + cy] += 1

  total += 1
}

puts h.count { |val| val >= 2 }
