#!/bin/sh

find . -type f | entr ./run.sh "$@"
