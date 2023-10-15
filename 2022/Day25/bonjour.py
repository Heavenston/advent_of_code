def snafu_to_decimal(snafu: str) -> int:
  lookup = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2,
  }

  out = 0
  for number_place, snafu_value in enumerate(reversed(snafu)):
    place_value = 5 ** number_place
    decimal_value = lookup[snafu_value]
    out += decimal_value * place_value

  return out


def decimal_to_snafu(decimal: int) -> str:
  lookup = {
    2: '2',
    1: '1',
    0: '0',
    -1: '-',
    -2: '=',
  }

  def chone(v):
    return (v + 1) // 2 - 1

  out = {}

  while decimal:
    number_place = 0
    while True:
      max_value_for_next_number_place = (5 ** (number_place + 1))
      ch = chone(max_value_for_next_number_place)
      if abs(decimal) > ch:
        number_place += 1
      else:
        break

    max_value_for_number_place = (5 ** number_place)
    value = 0

    if decimal > 0:
      while decimal > chone(max_value_for_number_place):
        decimal -= 5 ** number_place
        value += 1
    else:
      while decimal < -chone(max_value_for_number_place):
        decimal += 5 ** number_place
        value -= 1

    assert value in lookup
    snafu_value = lookup[value]
    assert number_place not in out
    out[number_place] = snafu_value
  
  out_str = ''
  for i in range(max(out.keys()) + 1):
    char = out[i] if i in out else '0'
    out_str += char

  out_str = ''.join(reversed(out_str))
  return out_str

part1_decimal = 0

i = """
1--
1-
1--02
1122-=2-==0-0=1-2
2=1-==-1022=10
1==-02211022=000
101==210-21=2
11010==0==221=0=02
11=1101020=02-11
1===
10-2
10=02=-=02
1-1--112-202--0
11-=-0-002=0112-1
2--0-2=02=-22
1001-2
1=101=2=2102-201--1
1-2==1100--
2-01=--=1-11
101-=0010-210==
1=-21-022121110
1==21
22==1
2-0-=2=1
2--0=10-00--2-
1--1=011-2
1-100-2
11-1
112
222200110-11110-2=
1==2-210-1122=-2022
2==1-20-2-=-21
21=1-=0=-1-=-=-12
210---=-1===-===00
1--21=01-022=2-
11-=
21-2
2-22-0
1==-
1-----01
1-0-21-
211212-22-12--=2
1=220=10=20200-0
21-=11-==20=1
102-2==2-==-0
1=0=01-
22=1--0111
1-----=1==00===0-
20==-1-121-
1=--2--21-202=21
1-0122=--=
2==-2--===-=-1=-012
2220=-00-10-
1==0=---10212-1-
1221=-022120
100112
2-=0=220-=01-1=12-
1=00
2122121=2
2-==
12-21===10220
1=0
22-1=--01-==0
1-2-2202=1=02
11-===21-
1-22=0102-=-222-1
1021=0=21=0=11=2-2
1===2222=0-0=
20=2-=0=
1=2==02-1-100200
1=1211211----
12=1=1---=20
2--2=2=1100020200
1=0-002-11-10----
1=1=-1=-0
1-21=1=02=21=20
1-=0-002-0=--=0=
20-===-1=
220021012
12===1001=--=2=1-
1=-02
21
2=200222122
1-2=110111=012=1-
1=02=
101==1-=1=0001
1=22--1-021
120
201-0211
1-1012211--2=-1=
12=10202=20
11-22=2=2=-0==1=00
11=-
12-1--2222
22
1120--0==
10=-0=001-
1=00200200=
1-20
1-0-
10112-202=-011
11-2=
1-=10=1-0=-21==11200
11
12-0-=01--12
1-=1121-=0
120-21=-1=10121=
1102-22
21=
1==--1==---1-==
12=0--=2210-1==
22210=1-=0
1102-20-1
1=1=2102
11--=2==-0
2=0=1=
21-0-10=
12-212-2=-==102--
1==0100210-=
12210-0-1
1=0-2-0=
10-1=211=1-2=
201-0--
1--2=00=-1-211
121=-22100=210--
122-0-1-
2=211
2=1-=2-2-0001=-1
1102--11=0=1=10==2
1==01121-2--0=12
2=21-20=-0-0
2-212=21-02=1-2-02
2=1-0
10-0-=20
2=2=201
"""
# i is the puzzle input
# it's just pasted above in the file
for snafu in i.strip().split('\n'):
  part1_decimal += snafu_to_decimal(snafu)

part_1 = decimal_to_snafu(part1_decimal)
print(part_1)
