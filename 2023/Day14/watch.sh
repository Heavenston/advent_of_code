#!/bin/sh

find . -type f | entr -cc ./run.sh "$@"
