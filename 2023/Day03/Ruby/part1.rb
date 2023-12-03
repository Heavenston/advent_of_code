input = STDIN.read
lines = input.split("\n")

def numeric?(lookAhead)
  lookAhead.match?(/[[:digit:]]/)
end

h = lines.map { |x| x.chars }

# puts h.to_s

alls = {}

(0...h.length).each { |rowi|
  row = h[rowi]
  (0...row.length).each { |coli|
    if not numeric?(row[coli])
      next
    end

    nstart = coli
    while nstart > 0 and numeric?(row[nstart - 1])
      nstart -= 1
    end
    nend = nstart
    while row[nend + 1] != nil and numeric?(row[nend + 1])
      nend += 1
    end

    (-1..1).each { |drow|
      (-1..1).each { |dcol| 
        r = rowi + drow
        c = coli + dcol
        if r < 0 or r >= h.length
          next
        end
        if c < 0 or c >= h[r].length
          next
        end
        # if not h[r][c] == nil
        #   next
        # end
        unless numeric?(h[r][c]) or h[r][c] == "."
          alls[[rowi, nstart]] = nend
          # printf "%d %d\n", nstart, nend
        end
      }
    }
  }
}

t = 0
alls.each { |key, nend|
  if not key
    next
  end
  row, nstart = key
  k = ""
  (nstart..nend).each { |i|
    k += h[row][i]
  }
  t += Integer(k)
}

puts t
