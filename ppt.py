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

class PPT():
	# Matrix due to F.M.J. Barning
	A = [[1,-2,2],[2,-1,2],[2,-2,3]]
	B = [[1,2,2],[2,1,2],[2,2,3]]
	C = [[-1,2,2],[-2,1,2],[-2,2,3]]
	ABC = [A,B,C]
	# initial primitive
	p = [3,4,5]
	# output vectors
	q = [[0,0,0],[0,0,0],[0,0,0],[]]
	
	
	def __init__(self,triple = [3,4,5]):
		if self.is_ppt(triple):
			self.p = triple
	
	def is_ppt(self,triple):
		a = triple[0]
		b = triple[1]
		c = triple[2]
		if gcd(a,b,c) != 1:
			return False
		elif a%2 == b%2:
			return False
		elif a*a + b*b != c*c:
			return False
		else:
			return True
			
	def gen_child_triples(self, triple, selector='B'):
		# Return a list of 3 child triples and root triple
		if self.is_ppt(triple):
			self.p = triple
			if selector == 'B':
				for row in range(3):
					self.q[0][row] = 0
					self.q[1][row] = 0
					self.q[2][row] = 0
					for col in range(3):
						self.q[0][row] += self.A[row][col] * self.p[col]
						self.q[1][row] += self.B[row][col] * self.p[col]
						self.q[2][row] += self.C[row][col] * self.p[col]
				self.q[3] = triple
				# Adjust format of result if required
				if self.q[0] > self.q[1]:
					self.q[0] ^= self.q[1]
					self.q[1] ^= self.q[0]
					self.q[0] ^= self.q[1]
				return self.q
							
			elif selector == 'P':
				return 0
				
			else:
				return 0
		else:
			print(triple, "Input triple is not primitive")
			return 0
		
		
		return 0

def main(args):
	
	# Test code goes here
	ppt = PPT()
	print(ppt.gen_child_triples([3,4,5],'B'))
	
	print(ppt.gen_child_triples([5,12,13],'B'))
	
	print(ppt.gen_child_triples([20,21,29],'B'))
	
	print(ppt.gen_child_triples([8,15,17],'B'))
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
