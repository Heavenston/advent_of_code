#!/bin/sh

while ! ./download.sh; do sleep 0.5; clear; done; clear; ./summarize.sh $@
