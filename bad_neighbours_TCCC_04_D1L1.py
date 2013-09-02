'''
ACCEPTED
Problem Statement
    	
The old song declares "Go ahead and hate your neighbor", and the residents of
 Onetinville have taken those words to heart. Every resident hates his next-door
  neighbors on both sides. Nobody is willing to live farther away from the town's
   well than his neighbors, so the town has been arranged in a big circle around
    the well. Unfortunately, the town's well is in disrepair and needs to be
     restored. You have been hired to collect donations for the Save Our Well fund.

Each of the town's residents is willing to donate a certain amount,
 as specified in the int[] donations, which is listed in clockwise order
  around the well. However, nobody is willing to contribute to a fund to which
   his neighbor has also contributed. Next-door neighbors are always listed 
   consecutively in donations, except that the first and last entries in donations
    are also for next-door neighbors. You must calculate and return the maximum amount
     of donations that can be collected.
Definition
Class:	BadNeighbors
Method:	maxDonations
Parameters:	int[]
Returns:	int
Method signature:	int maxDonations(int[] donations)
(be sure your method is public)
'''
class BadNeighbors:
	'''
	O(n^2) dp solution
	'''
	def maxDonations(self, sequence):
		if not sequence: return 0
		if len(sequence) < 4: return max(sequence)
		maxDon = [x for x in sequence]
		for i in xrange(2,len(sequence)-1):
			for j in xrange(0,i-1):		
				if maxDon[j]+sequence[i] > maxDon[i]:
					maxDon[i] = maxDon[j] + sequence[i]
	
		maxDon1 = [x for x in sequence]
		for i in xrange(2,len(sequence)):
			for j in xrange(1,i-1):		
				if maxDon1[j]+sequence[i] > maxDon1[i]:
					maxDon1[i] = maxDon1[j] + sequence[i]
		maxDon[len(sequence)-1] = maxDon1[len(sequence)-1]

		return max(maxDon)

if __name__ == "__main__":
	bn = BadNeighbors()
	print bn.maxDonations((10, 3, 2, 5, 7, 8)) 
	print bn.maxDonations((11, 15)) 
	print bn.maxDonations(( 7, 7, 7, 7, 7, 7, 7))
	print bn.maxDonations((1, 2, 3, 4, 5, 1, 2, 3, 4, 5)) 
	print bn.maxDonations((94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,  6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72))