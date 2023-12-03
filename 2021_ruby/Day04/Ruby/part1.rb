input = STDIN.read
lines = input.split("\n")

numbers = lines[0].split(",").map{ |x| Integer(x) }

# puts numbers.to_s

$rows = lines[2..].chunk_while { |x| x != "" } 
  .map { |x| x.filter { |i| i != "" }.map { |y|
    y.split(" ").map { |z| Integer(z.strip) }
  }}
$cols = $rows.map { |x| x.transpose }

# puts $rows.to_s
# puts $cols.to_s

def find_winner
  $rows.each_index { |index|
    player = $rows[index]
    player.each { |row|
      if row.length == 0
        yield index
      end
    }
  }
  $cols.each_index { |index|
    player = $cols[index]
    player.each { |col|
      if col.length == 0
        yield index
      end
    }
  }
end

numbers.each { |n|
  $rows = $rows.map { |a| a.map { |b| b.filter { |c| c != n } } }
  $cols = $cols.map { |a| a.map { |b| b.filter { |c| c != n } } }
  x = []
  find_winner { |winner|
    s = $rows[winner].flatten.sum
    x.push(s * n)
  }
  if x.length > 0
    puts x.to_s
    return
  end
}
