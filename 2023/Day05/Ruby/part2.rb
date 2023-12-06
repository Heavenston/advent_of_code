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

def push_if_valid_range(in_, range)
  start, length = range
  if start >= 0 and length > 0
    in_.push(range)
  end
end

def range_and(a, b)
  # printf "%s and %s: ", a.to_s, b.to_s

  start1, l1 = a
  end1 = start1 + l1
  start2, l2 = b
  end2 = start2 + l2

  start = [start1, start2].max
  end_ = [end1, end2].min
  # no overlap
  if start >= end_
    # printf "no overlap\n"
    return nil
  end

  # printf "overlap (%d, %d)\n", start, end_ - start
  return [start, end_ - start]
end

def range_remove(from, that)

  start1, l1 = from
  end1 = start1 + l1
  start2, l2 = that
  end2 = start2 + l2

  overlap = range_and(from, that)
  if overlap.nil?
    return [from]
  end

  # printf "%s - %s: ", from.to_s, that.to_s
  ostart, ol = overlap
  oend = ostart + ol

  alls = []
  # before overlap
  if start1 < start2
    alls.push([start1, [start2, end1].min - start1])
  end
  if end1 > end2
    s = [start1, end2].max
    alls.push([s, end1 - s])
  end

  # printf "all: %s\n", alls.to_s

  return alls
end

def map(range, map_ranges)
  # printf "mapping %s in %s\n", range.to_s, map_ranges.to_s

  out_ranges = []
  ranges = [range]

  map_ranges.each { |map_r|
    dest, from, size = map_r
    new_ranges = []

    # printf "$: %s\n", ranges.to_s

    ranges.each { |range|
      # printf ": %s\n", range.to_s
      overlap = range_and(range, map_r[1..])
      if not overlap.nil?
        out_ranges.push([overlap[0] - from + dest, overlap[1]])
      end

      # push non-ovelaps
      range_remove(range, map_r[1..]).each { |x| new_ranges.push(x) }
    }

    ranges = new_ranges
  }

  # printf "mapped res: %s\n", ranges.to_s

  ranges.push(*out_ranges)
  return ranges
end


# curr = seeds.map { |x| ["seed", x] }
curr = []
begin
  i = 0
  while i < seeds.length
    if i % 2 == 0
      curr.push([seeds[i]])
    else
      curr[curr.length - 1].push(seeds[i])
    end
    i += 1
  end
end

curr = curr.map { |x| ["seed", x] }

puts curr.to_s

dodo = true
while dodo
  dodo = false

  new = []

  curr.each { |c|
    curr_map, val = c
    # printf "val: %s\n", val.to_s
    if curr_map == "location"
      new.push(c)
      next
    end
    dodo = true

    map(val, maps[curr_map]).each { |n|
      new.push([tos[curr_map], n])
    }
  }

  # printf "new %s\n", new.to_s

  curr = new
end

# puts curr.to_s
# puts curr.map { |x| x[1] }.to_s
puts curr.map { |x| x[1][0] }.min
