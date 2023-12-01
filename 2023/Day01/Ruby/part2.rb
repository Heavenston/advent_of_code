input = STDIN.read
lines = input.split("\n")

# vals = lines.map { |x| Integer(x) }
vals = lines

def numeric?(lookAhead)
  lookAhead.match?(/[[:digit:]]/)
end

total = 0
vals.each { |val|
  val = val.gsub(/one/, "o1ne")
  val = val.gsub(/two/, "t2wo")
  val = val.gsub(/three/, "thr3ee")
  val = val.gsub(/four/, "fo4ur")
  val = val.gsub(/five/, "fi5ve")
  val = val.gsub(/six/, "s6ix")
  val = val.gsub(/seven/, "sev7en")
  val = val.gsub(/eight/, "eig8ht")
  val = val.gsub(/nine/, "ni9ne")
  # puts val
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
