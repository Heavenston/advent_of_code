#!/bin/sh

clear

echo "test:"
cat test.txt | ruby Ruby/part$1.rb

echo -e "\n\ninput:"
cat input.txt | ruby Ruby/part$1.rb
