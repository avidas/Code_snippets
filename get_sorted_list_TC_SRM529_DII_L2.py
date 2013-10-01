class KingSort:
	'''
	You are given a String[] kings. Each element of kings is the name of one king.
 	The name of each king consists of his actual name, a single space, and a Roman numeral.
  	Return a String[] containing the names rearranged into their proper order: that is,
   	the kings have to be in ascending lexicographic order according to their actual name, 
	and kings with the same name have to be in the correct numerical order.
	'''
	def getSortedList(self,kings):
		'''
		String parsing, sorting, lambda
		'''
		tens = ['','X','XX','XXX','XL','L']
		ones = ['', 'I','II','III','IV','V','VI','VII','VIII','IX']
		count, roman_to_dec = 0, {}
		for t in tens:
			for o in ones:
				roman_num = t + o
				roman_to_dec[roman_num] = count
				count += 1

		kings_split = []
		for k in kings:
			kt = k.split(" ")
			kings_split.append(kt)
		kings_split.sort(key=lambda (x,y) : x)

		kings_sorted = []
		start = 0
		while start < len(kings):
			end = start
			kn = kings_split[start][0]
			while end < len(kings) and kings_split[end][0] == kn:
				end += 1	
			kst = sorted(kings_split[start:end], key= lambda (x,y) : 
														roman_to_dec[y])
			
			for k in kst:
				kings_sorted.append(k[0]+" "+k[1])
			start = end

		return tuple(kings_sorted)

if __name__ == "__main__":
	ks = KingSort()
	print ks.getSortedList(("Richard III", "Richard I", "Richard II"))
	print ks.getSortedList(("John I", "John V", "John X", "John L"))
	print ks.getSortedList(("Louis IX", "Philippe II"))
	print ks.getSortedList(("Philippe VI", "Jean II", "Charles V", "Charles VI", "Charles VII", "Louis XI"))
	print ks.getSortedList(("Philippe II", "Philip II"))

