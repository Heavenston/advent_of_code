input = STDIN.read
lines = input.split("\n")

# vals = lines.map { |x| Integer(x) }
vals = lines

def numeric?(lookAhead)
  lookAhead.match?(/[[:digit:]]/)
end

total = 0
vals.each { |val|
  # printf "%d: %s\n", total, val
  a, *rest, b = val.chars.filter { |x| numeric?(x) }
  if a == nil
    a = b
  end
  if b == nil
    b = a
  end
  total += Integer(a + b)
}
puts total
