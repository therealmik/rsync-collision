#!/usr/bin/python

import sys
import os

BLOCKSIZE=700

##############################
#### Checksums and Hashes ####
##############################


class RollSum(object):
	def __init__(self):
		self.count = 0
		self.A = 0
		self.B = 0

	def set(self, value, count):
		self.A = value & 0xffff
		self.B = (value >> 16) & 0xffff
		self.count = count
	
	def rotate(self, inch, outch):
		"""perform a rollin and rollout"""
		self.A = (self.A + inch - outch) % 65536
		self.B = (self.B + self.A - (self.count * outch)) % 65536

	def rollin(self, inch):
		"""Add the byte value to A, then add A to B"""
		self.A = (self.A + inch) % 65536
		self.B = (self.B + self.A) % 65536
		self.count += 1

	def rollout(self, outch):
		"""Subtract the byte value from A, then subtract it self.count times from B.  Assumes it was the last char in"""
		self.A = (self.A - outch) % 65536
		self.B = (self.B - (self.count * outch)) % 65536
		self.count -= 1

	def sum(self):
		return (self.B << 16) | self.A

def faster_rollsum(A, B, data):
	for d in data:
		A += d
		B += A
	return (A & 0xffff) | ((B & 0xffff) << 16)

def main():
	for fn in sys.argv[1:]:
		data = list(map(ord, open(fn, "rb").read()))
		rollsum = faster_rollsum(0, 0, data)
		print "%08x %s" % (rollsum, fn)
		
if __name__ == "__main__":
	main()

