'''
ACCEPTED
Problem Statement
    	
You are planting a flower garden with bulbs to give you joyous
flowers throughout the year. However, you wish to plant the flowers
such that they do not block other flowers while they are visible.

You will be given a int[] height, a int[] bloom, and a int[] wilt.
Each type of flower is represented by the element at the same index of height,
bloom, and wilt. height represents how high each type of flower groyws, bloom
represents the morning that each type of flower springs from the ground,
and wilt represents the evening that each type of flower shrivels up and dies.
Each element in bloom and wilt will be a number between 1 and 365 inclusive,
and wilt[i] will always be greater than bloom[i]. You must plant all of 
the flowers of the same type in a single row for appearance, and you also
want to have the tallest flowers as far forward as possible. However, if a
flower type is taller than another type, and both types can be out of the
ground at the same time, the shorter flower must be planted in front of
the taller flower to prevent blocking. A flower blooms in the morning,
and wilts in the evening, so even if one flower is blooming on the same 
day another flower is wilting, one can block the other.

You should return a int[] which contains the elements of height in the order
you should plant your flowers to acheive the above goals. The front of the garden
is represented by the first element in your return value, and is where you view 
the garden from. The elements of height will all be unique, so there will always
be a well-defined ordering.
 
Definition
    	
Class:	FlowerGarden
Method:	getOrdering
Parameters:	int[], int[], int[]
Returns:	int[]
Method signature:	int[] getOrdering(int[] height, int[] bloom, int[] wilt)
(be sure your method is public)

#Idea : O n^2 search to seperate into list of lists , where each list represents a set of trees which 
overlap but do not overlap with trees in other lists. How it works is that we start from first element
and keep tally of current overall range eg 1-4 4-10 10-15 becomes 1-15 so if anything later falls in between
that would fall in the first group. We could just have another list to track which element  belongs to which
set. We can have initalizised to -1. 
and we keep going as along as there is a element with -1 in the list

 After doing so, we sort each sublist in ascending order and return merged list in descending order of first element of sublists. 

Not sure where the dp is , but this could work

'''

from itertools import chain
class FlowerGarden:
	'''
	Essentially solved with just simulation/data_structures
	'''
	def getOrdering(self,height,bloom,wilt):
		if len(height) < 2: return height
		hbw = sorted(zip(height,bloom,wilt), key=lambda (x,y,z): y)
		
		result_lists = []
		curr_low, curr_high, curr_index = hbw[0][1], hbw[0][2], 1
		result_entry = []
		result_entry.append(hbw[0][0]);

		while curr_index < len(height):
			if hbw[curr_index][1] <= curr_high:
				result_entry.append(hbw[curr_index][0])
				if hbw[curr_index][2] > curr_high:
					curr_high = hbw[curr_index][2]
			else:
				tmp_list = result_entry[:]
				result_lists.append(tmp_list)
				del result_entry[:]
				result_entry = [] 
				result_entry.append(hbw[curr_index][0])
				curr_low, curr_high = hbw[curr_index][1], hbw[curr_index][2]
			curr_index += 1

		if result_entry: result_lists.append(result_entry)
		for l in result_lists:
			l.sort()

		result_lists.sort(key=lambda x: x[0],reverse=True)
		print list(chain.from_iterable(result_lists))

if __name__ == "__main__":
	fg = FlowerGarden()
	fg.getOrdering((5,4,3,2,1),(1,1,1,1,1),(365,365,365,365,365))
	fg.getOrdering((5,4,3,2,1),(1,5,10,15,20),(4,9,14,19,24))
	fg.getOrdering((5,4,3,2,1),(1,5,10,15,20),(5,10,15,20,25))
	fg.getOrdering((5,4,3,2,1),(1,5,10,15,20),(5,10,14,20,25))
	fg.getOrdering((1,2,3,4,5,6),(1,3,1,3,1,3),(2,4,2,4,2,4))
	fg.getOrdering((3,2,5,4),(1,2,11,10),(4,3,12,13))




