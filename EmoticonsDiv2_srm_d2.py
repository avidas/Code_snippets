class EmoticonsDiv2(object):
	"""
	TC SRM 612 D2 L2
	http://community.topcoder.com/stat?c=problem_statement&pm=13041
	"""

	def printSmiles(self, smiles, count=0):
		"""
		Recursively return sum of smallest factors of smiles
		"""
		if smiles == 1:
			return count
		factor = 0
		for candidate in range(2, smiles+1):
			if smiles % candidate == 0:
				factor = candidate
				break
		return self.printSmiles(factor, count+(smiles/factor)) if (factor > smiles/factor and (smiles/factor > 1)) else self.printSmiles((smiles/factor), count+factor)

if __name__ == '__main__':
	ed = EmoticonsDiv2()
	print ed.printSmiles(2)
	print ed.printSmiles(6)
	print ed.printSmiles(11)
	print ed.printSmiles(16)
	print ed.printSmiles(1000)
