input = STDIN.read
lines = input.split("\n")

$h = {}
$size = 0
def count(x)
  $h = {}
  $size = 0
  x.each { |line|
    $size = [$size, line.length].max
    (0..line.length).each { |i|
      if not $h[i]
        $h[i] = [0, 0]
      end

      if line[i] == "0"
        $h[i][0] += 1
      else
        $h[i][1] += 1
      end
    }
  }
end

line_ox = lines.clone
bit = 0
count(line_ox)
while line_ox.length > 1 and bit < $size do
    line_ox = line_ox.filter { |l|
    if $h[bit][1] >= $h[bit][0]
      l[bit] == "1"
    else
      l[bit] == "0"
    end
  }

  count(line_ox)
  bit += 1
end
ox = line_ox[0]
puts ox

line_co = lines.clone
bit = 0
count(line_co)
while line_co.length > 1 and bit < $size do
  line_co = line_co.filter { |l|
    if $h[bit][0] <= $h[bit][1]
      l[bit] == "0"
    else
      l[bit] == "1"
    end
  }

  bit += 1
  count(line_co)
end
co = line_co[0]
puts co

ox = Integer(ox, 2)
co = Integer(co, 2)
puts ox, co
puts ox * co
