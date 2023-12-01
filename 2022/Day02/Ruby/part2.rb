input = STDIN.read
lines = input.split("\n")

LOST = "lost"
DRAW = "draw"
WIN = "win"

trns = {
  "X" => LOST,
  "Y" => DRAW,
  "Z" => WIN,

  "A" => "R",
  "B" => "P",
  "C" => "C",
}

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
  ["R", DRAW] => "R",
  "RP" => LOST,
  ["P", LOST] => "R",
  "RC" => WIN,
  ["C", WIN] => "R",

  "PR" => WIN,
  ["R", WIN] => "P",
  "PP" => DRAW,
  ["P", DRAW] => "P",
  "PC" => LOST,
  ["C", LOST] => "P",

  "CR" => LOST,
  ["R", LOST] => "C",
  "CP" => WIN,
  ["P", WIN] => "C",
  "CC" => DRAW,
  ["C", DRAW] => "C",
}

total = 0
lines.each { |line|
  him, rslt = line.split(" ").map { |x| trns[x] }
  me = rslts[[him, rslt]]
  a = scores[me]
  b = scores[rslt]

  # printf "%s (%s %s) ~ %s => %d ~ %s => %d ~ %d\n", line, him, me, rslt, b, me, a, a + b
  # printf "%s ~ %s %s ~ %s ~ %d + %d = %d\n", line, me, him, rslts[me + him], a, b, a + b

  total += a + b
}
puts total
