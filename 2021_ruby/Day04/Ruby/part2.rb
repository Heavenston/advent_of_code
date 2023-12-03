input = STDIN.read
lines = input.split("\n")

numbers = lines[0].split(",").map{ |x| Integer(x) }

# puts numbers.to_s

$wins = {}
$wins.default = false
$rows = lines[2..].chunk_while { |x| x != "" } 
  .map { |x| x.filter { |i| i != "" }.map { |y|
    y.split(" ").map { |z| Integer(z.strip) }
  }}
$cols = $rows.map { |x| x.transpose }

# puts $rows.to_s
# puts $cols.to_s

def find_winner
  $rows.each_index { |index|
    if not $wins[index]
      player = $rows[index]
      player.each { |row|
        if row.length == 0
          $wins[index] = true
          yield index
        end
      }
    end
  }
  $cols.each_index { |index|
    if not $wins[index]
      player = $cols[index]
      player.each { |col|
        if col.length == 0
          $wins[index] = true
          yield index
        end
      }
    end
  }
end

last = 0
numbers.each { |n|
  $rows = $rows.map { |a| a.map { |b| b.filter { |c| c != n } } }
  $cols = $cols.map { |a| a.map { |b| b.filter { |c| c != n } } }
  scores = []
  find_winner { |w|
    scores.push($rows[w].flatten.sum * n)
  }
  if scores.length != 0 and scores.max != 0
    last = scores.max
  end
}
puts last
