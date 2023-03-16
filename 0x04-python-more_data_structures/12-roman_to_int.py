#!/usr/bin/python3
def roman_to_int(roman_string): 
	roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	int_string = list(map(lambda a: roman[a], list(roman_string)))
	for i in range(0, len(int_string) - 1 ):
		if int_string[i] < int_string[i+1]:
			int_string[i] *= -1
	return sum(int_string)
