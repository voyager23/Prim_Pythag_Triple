#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  prim_pyth_trip.py
#  
#  Copyright 2022 Mike <mike@pop-os>
#  
#  Intended to hold class definition for generating and manipulating
#  primitive pythagorean triples
#  Sources: Wikipedia Tree of Pythagorean Triples
#			YouTube, Mathologer
#

from math import gcd

class Primitive_Pythagorean_Triple():
	# Matrix due to F.M.J. Barning
	A = [[1,-2,2],[2,-1,2],[2,-2,3]]
	B = [[1,2,2],[2,1,2],[2,2,3]]
	C = [[-1,2,2],[-2,1,2],[-2,2,3]]
	ABC = [A,B,C]
	# initial primitive
	p = [3,4,5]
	# output vectors
	q = [[0,0,0],[0,0,0],[0,0,0]]
	
	
	def __init__(self,a,b,c):
		# expect 3 integers
		if self.is_ppt(a,b,c):
			self.p[0] = a
			self.p[1] = b
			self.p[2] = c		
	
	def is_ppt(self,a,b,c):
		if gcd(a,b,c) != 1:
			return False
		elif a%2 == b%2:
			return False
		elif a*a + b*b != c*c:
			return False
		else:
			return True
			
	def gen_child_triples(self, selector='B'):
		#TODO: input a triple, test is_ppt, set root triple
		if selector == 'B':
			for row in range(3):
				self.q[0][row] == 0
				self.q[1][row] == 0
				self.q[2][row] == 0
				for col in range(3):
					self.q[0][row] += self.A[row][col] * self.p[col]
					self.q[1][row] += self.B[row][col] * self.p[col]
					self.q[2][row] += self.C[row][col] * self.p[col]
			return self.q
						
		elif selector == 'P':
			return 0
			
		else:
			return 0
		
		
		return 0

def main(args):
	# Test code goes here
	ppt = Primitive_Pythagorean_Triple(3,4,5)
	print(ppt.gen_child_triples('B'))
	ppt = Primitive_Pythagorean_Triple(5,12,13)
	print(ppt.gen_child_triples('B'))
	ppt = Primitive_Pythagorean_Triple(20,21,29)
	print(ppt.gen_child_triples('B'))
	ppt = Primitive_Pythagorean_Triple(8,15,17)
	print(ppt.gen_child_triples('B'))
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
