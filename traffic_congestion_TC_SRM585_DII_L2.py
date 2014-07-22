class TrafficCongestionDivTwo(object):
	"""
	TC SRM 585 D2 L2
	http://community.topcoder.com/stat?c=problem_statement&pm=12697
	"""
	def __init__(self):
		super(TrafficCongestionDivTwo, self).__init__()
		self.numCarsStore = {}

	def theMinCars(self, treeHeight):
		"""
		Return smallest number of cars that takes to traverse bst
		with given treeHeight with no overlap or revisit
		"""
		if treeHeight < 2:
			return 1
		elif treeHeight in self.numCarsStore:
			# Memoization
			return self.numCarsStore.get(treeHeight)
		else:
			numCars = 1
			for i in xrange(treeHeight-1):
				numCars += 2*(self.theMinCars(i))
			self.numCarsStore[treeHeight] = numCars
			return numCars

if __name__ == "__main__":
	tc = TrafficCongestionDivTwo()
	print tc.theMinCars(1)
	print tc.theMinCars(2)
	print tc.theMinCars(3)
	print tc.theMinCars(10)
	print tc.theMinCars(60)