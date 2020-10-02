#!/usr/bin/env python3
n = int(input())
def fac(n):
	k = 1
	for i in range(1,n + 1):
		k *= i
	return k
print(fac(n))
