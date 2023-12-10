input = STDIN.read
lines = input.split("\n")

stres = ['A','K','Q','T','9','8','7','6','5','4','3','2','J'].reverse

ranks = {}

total = 0
lines.each { |line|
  card, bid = line.split(" ")
  bid = Integer(bid)

  into = nil

  ks = {}
  ks.default = card.chars.count { |c| c == 'J' }
  card.chars.each { |c| if c != 'J' then ks[c] += 1 end }
  # puts ks.to_s
  if ks.any? { |k, count| count == 5 }
    into = :fioak
  elsif ks.any? { |k, count| count == 4 }
    into = :fooak
  elsif ks.length == 2 and ks.any? { |k, count| count == 3 }
    into = :full
  elsif ks.any? { |k, count| count == 3 }
    into = :thoak
  elsif ks.count { |k, count| count == 2 } == 2
    into = :tp
  elsif ks.length == 4 and ks.any? { |k, count| count == 2 } and ks.all? { |k, count| count == 2 or count == 1 }
    into = :op
  elsif ks.length == 5
    into = :hk
  end

  if not into
    next
  end
  if not ranks[into]
    ranks[into] = []
  end
  ranks[into].push([card, bid])
}

# puts ranks.to_s

rks_sort = [
  :fioak,
  :fooak,
  :full,
  :thoak,
  :tp,
  :op,
  :hk
]

ranks.each { |k, cards|
  cards.sort! { |a, b|
    a = a[0]
    b = b[0]
    x = 0
    a.chars.zip(b.chars).each { |a|
      ac, bc = a
      ai = stres.index(ac)
      bi = stres.index(bc)
      if ai > bi
        x = 1
        break
      elsif bi > ai
        x = -1
        break
      end
    }
    # printf "%s - %s = %d\n", a, b, x
    x
  }
  # puts cards.to_s
}

i = 1
total = 0
rks_sort.reverse.each { |k|
  cards = ranks[k]
  if not cards
    next
  end
  cards.each { |card|
    card, bid = card
    total += bid * i
    # printf "%s -> %d\n", card, i
    i += 1
  }
}
puts total
