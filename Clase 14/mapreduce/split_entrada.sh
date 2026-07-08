#!/usr/bin/bash
mkdir -p splits
split -l 33 -d --additional-suffix=.txt entrada.txt splits/part_