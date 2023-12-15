require "matrix"

input = STDIN.read
lines = input.split("\n")

total = 0

def hash(x)
  s = 0
  x.chars.each { |x| 
    s += x.ord
    s = (s * 17) % 256
  }
  s
end

boxes = {}

lines[0].split(",").map { |l|
  n = l[-1] == "-" ? l[...-1] : l.split("=")[0]
  # puts n

  h = hash(n)
  b = boxes[h]
  if not b
    boxes[h] = []
    b = boxes[h]
  end

  j = nil
  b.each_index { |i|
    if b[i][0] == n
      j = i
    end
  }

  puts l
  if l[-1] == "-"
    if j
      b.delete_at j
    end
  else
    v = Integer(l.split("=")[1])

    if j
      b[j][1] = v
    else
      b.push([n, v])
    end
  end

  puts boxes.to_s
}

boxes.each { |k, v|
  v.each_with_index { |q, i|
    n, v = q
    sc = (k + 1) * (i + 1) * v
    printf "[%d][%d] %s %d = %d\n", k, i, n, v, sc
    total += sc
  }
}

puts total
File.write(ENV["SOLUTION_FILE"], total.to_s)
