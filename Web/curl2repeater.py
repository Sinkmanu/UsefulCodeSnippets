#!/usr/bin/env python3

import sys

# Command: curl -vs http://unam.re 2>&1  | python3 curl2repeater.py

data = sys.stdin.readlines()
print("[*] Copy the following command:")
for i in data:
    if (i[0] == ">"):
        print(i[1:].replace("\r\n","").strip())
print("\n")
