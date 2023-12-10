input = STDIN.read
lines = input.split("\n")

vals = lines.map { |line| line.split(" ").map { |x| Integer(x) } }

puts vals.to_s

total = 0
vals.each { |ls|
  news = []
  f = false
  until f
    f = true

    new = []
    use_ = news[-1] ? news[-1] : ls
    (0...(use_.length - 1)).each { |i|
      if use_[i + 1] - use_[i] != 0
        f = false
      end
      new.push(use_[i + 1] - use_[i])
    }
    news.push(new)
  end
  puts news.to_s

  preds = [0]
  news.reverse.each { |new|
    preds.push(preds[-1] + new[-1])
  }
  preds.push(preds[-1] + ls[-1])
  puts preds.to_s
  total += preds[-1]
}
puts total
