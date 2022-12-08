# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 11:40:12 2022

@author: japem
"""
# part 1
file = open("input.txt")
elves = file.read().split("\n\n")[:-1]
elves = [elf.split("\n") for elf in elves]

calories = [0 for i in range(len(elves))]
for i, elf in enumerate(elves):
    for calorie in elf:
        calories[i] += int(calorie)

ind = 0
cal = 0
for i, calorie in enumerate(calories):
    if calorie > cal:
        ind = i
        cal = calorie
