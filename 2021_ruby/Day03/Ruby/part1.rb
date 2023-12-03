input = STDIN.read
lines = input.split("\n")

h = {}

size = 0
lines.each { |line|
  size = [size, line.length].max
  (0..line.length).each { |i|
    if not h[i]
      h[i] = [0, 0]
    end

    if line[i] == "0"
      h[i][0] += 1
    else
      h[i][1] += 1
    end
  }
}

eps = ""
gam = ""
(0..(size - 1)).each { |i|
  if h[i][0] > h[i][1]
    eps += "0"
    gam += "1"
  else
    eps += "1"
    gam += "0"
  end
}

puts Integer(eps, 2) * Integer(gam, 2)
