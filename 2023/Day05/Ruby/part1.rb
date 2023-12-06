require "matrix"

input = STDIN.read
lines = input.split("\n")

seeds = lines[0].split(": ")[1].split(" ").map { |x| Integer(x) }

maps_l = lines[2..].chunk_while { |x| x != "" }.map { |x| x.filter { |y| y != "" } }

maps = { }
tos = {}
maps_l.each { |l|
  name, *vals = l
  from, to = name.split(" ")[0].split("-to-")
  maps[from] = vals.map{ |x| x.split(" ").map { |z| Integer(z) } }
  tos[from] = to
}

puts tos.to_s
puts maps.to_s

def map(x, ranges)
  ranges.each { |r|
    to, from, size = r
    if x >= from and (x - from) <= size
      return to + (x - from)
    end
  }
  return x
end

curr = seeds.map { |x| ["seed", x] }

dodo = true
while dodo
  dodo = false

  new = []
  curr.each { |c|
    curr_map, val = c
    if curr_map == "location"
      new.push(c)
      next
    end
    dodo = true

    new.push([tos[curr_map], map(val, maps[curr_map])])
  }

  curr = new
end

puts curr.min
