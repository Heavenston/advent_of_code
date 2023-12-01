#!/bin/sh

echo -e "test:"
cat test.txt | ruby Ruby/part$1.rb
echo -e "\n\n\ninput:"
cat input.txt | ruby Ruby/part$1.rb
