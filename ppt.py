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

from math import gcd, sqrt

class PPT():
	# Matrix due to F.M.J. Barning
	A = [[1,-2,2],[2,-1,2],[2,-2,3]]
	B = [[1,2,2],[2,1,2],[2,2,3]]
	C = [[-1,2,2],[-2,1,2],[-2,2,3]]
	ABC = [A,B,C]
	
	# Matrix due to H Lee Price
	PA = [[2,1,-1],[-2,2,2],[-2,1,3]]
	PB = [[2,1,1],[2,-2,2],[2,-1,3]]
	PC = [[2,-1,1],[2,2,2],[2,1,3]]
	
	# Matrix for Euclid sequence
	EA = [[2,-1],[1,0]]
	EB = [[2,1],[1,0]]
	EC = [[1,2],[0,1]]
	

	# initial primitive
	p = [3,4,5]
	# output list of children + root triple
	q = [[0,0,0],[0,0,0],[0,0,0],[]]
	
	
	def __init__(self,triple = [3,4,5]):
		if self.is_ppt(triple):
			self.p = triple
		else:
			print("Input data is invalid. Using [3,4,5]")
	
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
			if selector == 'B':		# Matrix due to F.M.J. Barning
				for row in range(3):
					self.q[0][row] = 0
					self.q[1][row] = 0
					self.q[2][row] = 0
					for col in range(3):
						self.q[0][row] += self.A[row][col] * self.p[col]
						self.q[1][row] += self.B[row][col] * self.p[col]
						self.q[2][row] += self.C[row][col] * self.p[col]
				self.q[3] = triple
				'''
				# Adjust format of result if required
				if self.q[0] > self.q[1]:
					self.q[0] ^= self.q[1]
					self.q[1] ^= self.q[0]
					self.q[0] ^= self.q[1]
				'''
				return self.q
							
			elif selector == 'P':	# Matrix due to H Lee Price
				for row in range(3):
					self.q[0][row] = 0
					self.q[1][row] = 0
					self.q[2][row] = 0
					for col in range(3):
						self.q[0][row] += self.PA[row][col] * self.p[col]
						self.q[1][row] += self.PB[row][col] * self.p[col]
						self.q[2][row] += self.PC[row][col] * self.p[col]
				self.q[3] = triple
				'''
				# Adjust format of result if required
				if self.q[0] > self.q[1]:
					self.q[0] ^= self.q[1]
					self.q[1] ^= self.q[0]
					self.q[0] ^= self.q[1]
				'''
				return self.q
							
			else:
				print("Matrix selector unknown.")
				return 0
		else:
			print(triple, "Input triple is not primitive")
			return 0
			
	def is_valid_mn(self, mn):
		# expect list [m,n]
		m = mn[0]
		n = mn[1]
		return ((m > n) and gcd(m,n) == 1 and (m%2 != n%2))
		
	def recover_mn(self, triple):
		# a = m^2 - n^2		b = 2mn		c = m^2 + n^2
		if self.is_ppt(triple):
			m = sqrt((triple[0]+triple[2]) / 2)
			n = triple[1]/(2*m)
			return [int(m),int(n)]
			
		else:
			print("Recover_mn invalid triple.")
			return [0,0]
			
	def euclid_triples(self, triple):
		mn = self.recover_mn(triple)	#[m,n]
		self.q = [[0,0,0],[0,0,0],[0,0,0],[]]
		child_mn = [[0,0],[0,0],[0,0]]
		for row in range(2):
			for col in range(2):
				child_mn[0][row] += self.EA[row][col] * mn[col]
				child_mn[1][row] += self.EB[row][col] * mn[col]
				child_mn[2][row] += self.EC[row][col] * mn[col]
		for i in range(3):
			self.q[i][0] = child_mn[i][0]**2 - child_mn[i][1]**2			
			self.q[i][1] = 2 * child_mn[i][0] * child_mn[i][1]			
			self.q[i][2] = child_mn[i][0]**2 + child_mn[i][1]**2
		return self.q			
			
			
	'''
	def euclid_sequence(self, mn, count = 1):
		self.q.clear()
		if self.is_valid_mn(mn):
			m = mn[0]	# convenience variables
			n = mn[1]
			while count:
				t = [0,0]
				self.q.append([m*m - n*n , 2*m*n , m*m + n*n])
				# update m & n values by matrix multiply
				t[0] = self.E[0][0]*m + self.E[0][1]*n
				t[1] = self.E[1][0]*m + self.E[1][1]*n
				m = t[0]
				n = t[1]
				count -=1
			return self.q
		else:
			print("m and/or n invalid")
			return self.q
	'''
		
def main(args):
	
	# Test code goes here
	ppt = PPT()
	print(ppt.gen_child_triples([3,4,5],'P'))	
	print(ppt.gen_child_triples([5,12,13],'P'))	
	print(ppt.gen_child_triples([15,8,17],'P'))	
	print(ppt.gen_child_triples([7,24,25],'P'))	
	
	#print(ppt.euclid_triples([20,21,29]))
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
