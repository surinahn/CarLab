#!/bin/bash

sudo ./hello_pixy > output.txt 
awk -f clean.awk output.txt > cleaned.txt 