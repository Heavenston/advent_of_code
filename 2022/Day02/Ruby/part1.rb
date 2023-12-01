input = STDIN.read
lines = input.split("\n")

trns = {
  "X" => "R",
  "Y" => "P",
  "Z" => "C",

  "A" => "R",
  "B" => "P",
  "C" => "C",
}

LOST = "lost"
DRAW = "draw"
WIN = "win"

scores = {
  "R" => 1,
  "P" => 2,
  "C" => 3,

  LOST => 0,
  DRAW => 3,
  WIN => 6,
}

rslts = {
  "RR" => DRAW,
  "RP" => LOST,
  "RC" => WIN,

  "PR" => WIN,
  "PP" => DRAW,
  "PC" => LOST,

  "CR" => LOST,
  "CP" => WIN,
  "CC" => DRAW,
}

total = 0
lines.each { |line|
  him, me = line.split(" ").map { |x| trns[x] }
  a = scores[me]
  b = scores[rslts[me + him]]
  # printf "%s ~ %s %s ~ %s ~ %d + %d = %d\n", line, me, him, rslts[me + him], a, b, a + b
  total += a + b
}
puts total

