require "matrix"

input = STDIN.read
lines = input.split("\n")

ms = lines.map { |x| x.chars }.chunk_while { |x| x.length != 0 }.map { |x| x.filter { |y| y.length != 0 } }

h = {}
h.default = nil

total = 0

def is_ref_col(m, col)
  m.transpose.all? { |c|
#     printf "'%s'[%d]\n", c.join(""), col
    left = c[...col]
    rigt = c[col...]
#     printf "%d, '%s' '%s'\n", col, left.join(""), rigt.join("")

    size = [left.length, rigt.length].min
    left = left[(left.length - size)...].reverse
    rigt = rigt[...size]
#     printf "%d, '%s' == '%s'\n", size, left.join(""), rigt.join("")
    left.each_index.count { |i| left[i] != rigt[i] } == 1
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
#       printf "works for me %d\n", i
      return i
    end
  }
  return nil
end

def ffind(m)
  [find_col(m), find_row(m)]
end

def find(m)
  l = ffind(m)
  # change(m) { |m, i1, i2|
  #   nl = ffind(m)
    
  #   if not nl.all? { |x| x.nil? } and nl != l
  #     printf "SMUDGE, %d %d\n", i1, i2
  #     return [nl[0] == l[0] ? nil : nl[0], nl[1] == l[1] ? nil : nl[1]]
  #   end
  # }
  return l
end

# def change(m)
#   m.each_index { |i1|
#     m[i1].each_index { |i2|
#       v = m[i1][i2]
#       nv = ""
#       if v == "."
#         nv = "#"
#       elsif v == "#"
#         nv = "."
#       end
#       m[i1][i2] = nv
#       yield m, i1, i2
#       m[i1][i2] = v
#     }
#   }
# end

ms.each { |m|
  x = find(m)
  v = (x[0] ? x[0] : 0) + (x[1] ? x[1] : 1) * 100
  printf "TOTAL LINE %d\n", v
  
  total += v
}

printf "total: %d\n", total
File.write(ENV["SOLUTION_FILE"], total.to_s)
