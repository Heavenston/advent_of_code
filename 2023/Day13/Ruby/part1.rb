require "matrix"

input = STDIN.read
lines = input.split("\n")

ms = lines.map { |x| x.chars }.chunk_while { |x| x.length != 0 }.map { |x| x.filter { |y| y.length != 0 } }

h = {}
h.default = nil

total = 0

def is_ref_col(m, col)
  m.transpose.all? { |c|
    printf "'%s'[%d]\n", c.join(""), col
    left = c[...col]
    rigt = c[col...]
    printf "%d, '%s' '%s'\n", col, left.join(""), rigt.join("")

    size = [left.length, rigt.length].min
    left = left[(left.length - size)...].reverse
    rigt = rigt[...size]
    printf "%d, '%s' == '%s'\n", size, left.join(""), rigt.join("")
    left == rigt and left.length > 0 and rigt.length > 0
  }
end

def find_col(m)
  (0...m[0].length).each { |i|
    if is_ref_col(m.transpose, i)
      return i
    end
  }
  return nil
end

def find_row(m)
  (0...m.length).each { |i|
    if is_ref_col(m, i)
      printf "works for me %d\n", i
      return i
    end
  }
  return nil
end

def find(m)
  c = 0
  cc = find_col(m)
  if cc
    c += cc
  end
  cc = find_row(m)
  if cc
    c += cc * 100
  end
  c
end

ms.each { |m|
  x = find(m)
  printf "TOTAL LINE %d\n", x
  
  total += x
}

printf "total: %d\n", total
File.write(ENV["SOLUTION_FILE"], total.to_s)
