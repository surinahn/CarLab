#!/bin/bash

sudo ./hello_pixy > output.txt &
sleep 3s
sudo pkill -SIGINT hello_pixy
awk -f clean.awk output.txt > cleaned.txt