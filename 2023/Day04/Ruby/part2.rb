input = STDIN.read
lines = input.split("\n")

$scores = {}

news = []

def comp(win, mine)
  key = win.join(" ") + " | " + mine.join(" ")
  if $scores[key]
    return $scores[key]
  end

  val = 0

  mine.each { |w|
    in_ = win.any? { |m| w == m }
    if in_
      val += 1
    end
  }

  $scores[key] = val
  return val
end

ss = []

lines.each_index { |i|
  line = lines[i]
  # printf "%d: %s\n", total, line

  p1, p2 = line.split(": ")
  id = Integer(p1.split(" ")[1])
  win, mine = p2.split(" | ").map{ |s| s.split(" ").map { |x| Integer(x) } }

  # puts id, win, mine

  val = comp(win, mine)
  ss.push(val)
}

s = Array.new(ss.length, 1)
tt = Array.new(ss.length, 1)

dddd = true
while dddd

  ss.each_index { |i|
    rep = s[i]
    score = ss[i]
    (1..score).each { |di|
      dddd = false
      s[i + di] += rep
      tt[i + di] += rep
    }
    s[i] = 0
  }
end

puts tt.sum

i = 0
while news.length > i
  score = news[i]

  # puts win.join(" ") + " | " + mine.join(" ")
  # score = comp(win, mine)
  # puts score.to_s


  i += 1
  break
end

# puts news.length
