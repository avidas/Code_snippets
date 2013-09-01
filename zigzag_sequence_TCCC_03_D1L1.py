'''
ZigZag Problem

A sequence of numbers is called a zig-zag sequence if the differences between successive numbers
strictly alternate between positive and negative. The first difference (if one exists) may be
either positive or negative. A sequence with fewer than two elements is trivially a zig-zag
sequence.

For example, 1,7,4,9,2,5 is a zig-zag sequence because the differences (6,-3,5,-7,3) are
alternately positive and negative. In contrast, 1,4,7,2,5 and 1,7,4,5,5 are not zig-zag
sequences, the first because its first two differences are positive and the second because
its last difference is zero.

Given a sequence of integers, sequence, return the length of the longest subsequence of sequence
that is a zig-zag sequence. A subsequence is obtained by deleting some number of elements
(possibly zero) from the original sequence, leaving the remaining elements in their
original order.
'''

class ZigZag:
	'''
	DP solution
	'''
	def longestZigZag(self, sequence):
		if not sequence: return 0
		prev, maxlen = [-1 for x in sequence],[1 for x in sequence]

		for i in xrange(len(sequence)):
			for j in xrange(i):
				if sequence[i] != sequence[j] and prev[j] == -1 or (sequence[i] - sequence[j])*(sequence[j] - sequence[prev[j]]) < -1:
					if maxlen[j]+1 > maxlen[i]:
						maxlen[i] = maxlen[j]+1
						prev[i] = j
				
		return max(maxlen)


if __name__ == "__main__":
	zz = ZigZag()
	print zz.longestZigZag((1, 7, 4, 9, 2, 5))
	print zz.longestZigZag((1, 17, 5, 10, 13, 15, 10, 5, 16, 8))
	print zz.longestZigZag(())
	print zz.longestZigZag([-1])
	print zz.longestZigZag([1, 2, 3, 4, 5, 6, 7, 8, 9])
	print zz.longestZigZag([70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32])
	print zz.longestZigZag([374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 
		600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 
67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 
477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 
249, 22, 176, 279, 23, 22, 617, 462, 459, 244])