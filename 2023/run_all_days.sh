#!/bin/sh

DAYS="01 02 03 04 05 06 07 08 09"

echo "========================="
echo "=  Advent of code 2023  ="
echo "========================="


total_time_start_ms=$(date +%s%3N)
for num in $DAYS; do
    cd day$num
    time_start_task=$(date +%s%3N)
    python3 part1.py > /dev/null
    python3 part2.py > /dev/null
    time_task=$(($(date +%s%3N)-$time_start_task))
    echo "day$num: ${time_task}ms"
    cd ..
done
total_time_ms=$(($(date +%s%3N)-$total_time_start_ms))

echo "========================="
echo "Total runtime: $(($total_time_ms/1000))s ${total_time_ms}ms"
echo "========================="