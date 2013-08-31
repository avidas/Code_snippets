def merge_interval(low_priority_lst,high_priority_lst):
	'''
	Given two lists with date ranges, return merged list with high_priority_lst ranges preferred over
	low_priority_lst ranges in case of intersection.  Partial intervals are allowed.
	'''
	if low_priority_lst == [] or low_priority_lst == None: return high_priority_lst
	if high_priority_lst == [] or high_priority_lst == None: return low_priority_lst
	
	# k way merge interval, also may need to mark which array it belongs to
	# case :               |-------|
	#        |-------|            
	if low_priority_lst[0][0] > high_priority_lst[0][1]:
	 return [high_priority_lst[0]] + merge_interval(low_priority_lst,high_priority_lst[1:])
	# case :   |-------|
	#                     |-------|  	 
	elif low_priority_lst[0][1] < high_priority_lst[0][0]:
		return [low_priority_lst[0]] + merge_interval(low_priority_lst[1:],high_priority_lst)
	# case :|-------|
	#            |-------|  
	elif low_priority_lst[0][0] < high_priority_lst[0][0]:
		return [[low_priority_lst[0][0],high_priority_lst[0][0]]] + merge_interval( [[high_priority_lst[0][0],low_priority_lst[0][1]]] + low_priority_lst[1:],high_priority_lst)
	# case :      |-------|
	#        |-------|  
	elif low_priority_lst[0][1] > high_priority_lst[0][1]:
		return [high_priority_lst[0]] + merge_interval( [[high_priority_lst[0][1],low_priority_lst[0][1]]] + low_priority_lst[1:] , high_priority_lst[1:])
	# case :  |-------| |---| |----|
	#        |-----------------| 
	else:
		return merge_interval(low_priority_lst[1:],high_priority_lst)

if __name__ == '__main__':
	print merge_interval( [[200604,200606],[200608,200612],[200701,200712]] , [[200603,200605],[200609,200702]] )