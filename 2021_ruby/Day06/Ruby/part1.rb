input = STDIN.read
lines = input.split("\n")

ls = lines[0].split(",").map{ |x| Integer(x) }

h = {  }
h.default = 0

ls.each { |v|
  h[v] += 1
}

(0...256).each { |day|
  new = {}
  new.default = 0

  h.each { |timer, count|
    if timer == 0
      new[6] += count
      new[8] += count
    else
      new[timer - 1] += count
    end
  }

  h = new
}

puts h.each_value.sum
