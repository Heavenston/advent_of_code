#!/bin/sh

echo -e "$1:"
cat $1 | ruby Ruby/part$2.rb
