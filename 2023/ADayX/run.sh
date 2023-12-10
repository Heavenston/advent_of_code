#!/bin/sh

if [ $# -ne 2 ]
then
  echo missing input file or part name
  exit 1
fi

export INPUT_FILE="$1"
export PART_NAME="$2"
export SOLUTION_FILE="solution_part$PART_NAME.txt"

echo "$INPUT_FILE:"
cat "$INPUT_FILE" | ruby "Ruby/part$PART_NAME.rb"
