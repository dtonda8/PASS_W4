from typing import List, TypeVar
from data_structures.array_list import ArrayList
T = TypeVar("T")

def merge(list1: List[T], list2: List[T]) -> List[T]:
	p1 = 0
	p2 = 0
	n1 = len(list1)
	n2 = len(list2)
	ans = ArrayList(n1 + n2)

	while p1 < n1 and p2 < n2:
		if list1[p1] < list2[p2]:
			ans.append(list1[p1])
			p1 += 1
		else:
			ans.append(list2[p2])
			p2 += 1
	
	# Add leftover
	for i in range(p1, n1):
		ans.append(list1[i])
	
	for i in range(p2, n2):
		ans.append(list2[i])

	return ans

# if __name__ == "__main__": # for personal tests
# 	pass