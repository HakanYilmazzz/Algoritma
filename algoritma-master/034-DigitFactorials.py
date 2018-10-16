#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from math import factorial
sonuc = 0
for n in range(3,100000):
    toplam = 0
    for i in str(n):
        toplam += factorial(int(i))
    if n==toplam:
        sonuc += n
print(sonuc)
