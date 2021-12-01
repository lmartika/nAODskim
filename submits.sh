#!/bin/bash

input=$1

while IFS= read -r line

do
  echo "Submit $line"
  python crab_cfg_file.py $line

done < "$input"
