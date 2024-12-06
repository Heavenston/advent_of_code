require "matrix"

input = STDIN.read
lines = input.split("\n")

h = {}
h.default = nil

total = 0

def count(arras, l)
  lasti = 0
  chunks = l.chunk_while { |a, b|
    a == b or (a == "#" and b == "?") or (a == "?" and b == "#")
  }.filter { |chunk| not chunk.all? { |x| x == "." } }
    .each_with_index { |chunk, i|
    if chunk.any? { |x| x == "?" }
      break
    end
    if chunk.length != arras[i]
      return 0
    end
    lasti = i
  }

  nos = nil
  l.each_with_index { |c, i|
    if c != "?"
      next
    end
    nos = i
    break
  }

  if nos.nil?
    # puts l.join("")
    if lasti != arras.length - 1
      return 0
    end
    return 1
  end

  c = 0
  new1 = l.clone
  new1[nos] = "."
  c += count(arras, new1)
  new2 = l.clone
  new2[nos] = "#"
  c += count(arras, new2)

  return c
end

lines.each { |line|
  l, arras = line.split(" ")
  l = l.chars

  arras = arras.split(",").map { |x| Integer(x) }
  printf "%s\n", line
  c = count(arras, l)
  printf " = %d\n", c
  total += c
}

puts total
File.write(ENV["SOLUTION_FILE"], total.to_s)
