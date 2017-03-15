#!/usr/bin/python

def big_enough(x):
	if x > 5:
		return True
	else:
		return False


print filter(big_enough, [1,2,3,4,5,6,7,9,8,0])
