require "matrix"

input = STDIN.read
lines = input.split("\n")

h = {}
h.default = nil

total = 0

$hah = {}

def count(arras, l, i)
  lasti = 0
  chunks = l.chunk_while { |a, b|
    a == b or (a == "#" and b == "?") or (a == "?" and b == "#")
  }.to_a

  chunks.filter { |chunk| not chunk.all? { |x| x == "." } }
    .each_with_index { |chunk, i|
      if chunk.any? { |x| x == "?" }
        break
      end
      if chunk.length != arras[i]
        return 0
      end
      lasti = i
    }

  key = [lasti, l[i..]]
  if $hah[key]
    puts "hit"
    return $hah[key]
  end

  nos = nil
  (i...l.length).each { |i|
    if l[i] != "?"
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
  c += count(arras, new1, nos)
  new2 = l.clone
  new2[nos] = "#"
  c += count(arras, new2, nos)

  $hah[key] = c

  return c
end

lines.each { |line|
  ll, aarras = line.split(" ")
  ll = ll.chars
  aarras = aarras.split(",").map { |x| Integer(x) }

  l = []
  (0...5).each {
    l.push(*ll)
    l.push("?")
  }
  arras = aarras.cycle(5).to_a

  printf "%s\n", line
  $hah = {}
  c = count(arras, l, 0)
  printf " = %d\n", c
  total += c
}

puts total
File.write(ENV["SOLUTION_FILE"], total.to_s)
