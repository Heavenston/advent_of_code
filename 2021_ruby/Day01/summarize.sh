#!/bin/sh

if [ $# -ne 1 ]
then
  echo missing part $#
  exit 1
fi

PART=$1

cat puzzle.md chatgpt_req.txt | sed -e "s/#PART#/$1/g"
