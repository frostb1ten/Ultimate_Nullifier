#!/usr/bin/env python3
import time
import os
import sys

os.system('cls' if os.name == 'nt' else 'clear')

entity = sys.argv[1]
for number in range(1,100):
    time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Starting Attack...")
    print("--Hacking "+entity)
    print("Penetrating into the system...")
    print("Hacking "+entity+" "+str(number)+"%")
os.system('cls' if os.name == 'nt' else 'clear')
print(entity+" Hacked Successfully")
