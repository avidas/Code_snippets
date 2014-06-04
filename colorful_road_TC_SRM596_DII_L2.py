import sys

class ColorfulRoad:

	def getMin(self, road):
		"""
		Mininum cost to go from start to end on road given as "R[RGB]*". Cost going
		from i to j is (j-i)^2. A valid move is going forward and from R to G, G to
		B, or B to R.
		"""
		cost_track = [[sys.maxint]*len(road)]*len(road) 							# init with max int since min positive value required later
		order = ['R', 'G', 'B'] 													# for easy comparison for allowed moves
		for i in xrange(len(road)-1):
			for j in xrange(i+1, len(road)):
				if (order.index(road[j]) - order.index(road[i])) in [1,-2]:			# allowed move
					if i == 0: #
						cost_track[i][j] = (j-i)*(j-i) 								# from first step, any valid position is reachable
					else:
						if min([val[i] for val in cost_track]) != sys.maxint:		# if position i can be reached
							cost_track[i][j] = min(cost_track[i][j], (j-i)*(j-i) 	# min cost to reach i + getting from i to j < min cost to reach j
								+ min([val[i] for val in cost_track])) 
		if min([val[len(road) -1] for val in cost_track]) != sys.maxint:			# take min of all paths to reach end or return -1
			return min([val[len(road) -1] for val in cost_track])
		else: return -1

if __name__ == '__main__':
	cr = ColorfulRoad()
	print cr.getMin("RR")