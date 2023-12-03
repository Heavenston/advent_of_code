input = STDIN.read
lines = input.split("\n")

def numeric?(lookAhead)
  lookAhead.match?(/[[:digit:]]/)
end

h = lines.map { |x| x.chars }

# puts h.to_s

alls = {}

def get_num(h, rowi, coli)
  nstart = coli
  while nstart > 0 and numeric?(h[rowi][nstart - 1])
    nstart -= 1
  end
  nend = nstart
  while h[rowi][nend + 1] != nil and numeric?(h[rowi][nend + 1])
    nend += 1
  end
  [nstart, nend]
end

(0...h.length).each { |rowi|
  row = h[rowi]
  (0...row.length).each { |coli|
    if row[coli] != "*"
      next
    end
    
    nums = {}

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

        if not numeric?(h[r][c])
          next
        end
        
        nstart, nend = (get_num h, r, c)
        nums[[r, nstart]] = [r, c, nstart, nend]
      }
    }

    # puts nums.to_s
    if nums.length != 2
      next
    end

    alls[[rowi, coli]] = nums
  }
}

t = 0
alls.each { |key, nums|
  prod = 1

  nums.each_value { |v|
    rowi, coli, nstart, nend = v
    k = ""
    (nstart..nend).each { |i|
      k += h[rowi][i]
    }
    # puts k
    prod *= Integer(k)
  }

  t += prod
}

puts t
