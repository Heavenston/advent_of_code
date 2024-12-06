#!/bin/sh

if [ $# -ne 1 ]
then
  echo missing part name
  exit 1
fi

PART_NAME="$1"
SOLUTION_FILE="solution_part$PART_NAME.txt"
SOL=$(cat $SOLUTION_FILE)

echo "Submitting solution '$SOL' to part '$PART_NAME' of day '14'"

aoc submit $1 "$SOL" -y 2023 -d 14
