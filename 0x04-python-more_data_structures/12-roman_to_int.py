#!/usr/bin/python3
def roman_to_int(roman_string): 
	roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	ints = list(map(lambda a: roman[a], list(roman_string)))
	weights = list(map(lambda a: -1 if a[0] < a[1]  else 1, list(zip(ints[:-1], ints[1:])))) + [1]
	return sum(map(lambda a: a[0] * a[1], zip(ints, weights)))