from typing import List, TypeVar
from data_structures.queue_adt import CircularQueue
T = TypeVar("T")

def time_required_to_buy(tickets: List[T], k: int) -> int:
	## Using Lists
	# ans = 0
	# while tickets[k] > 0:
	# 	for i in range(len(tickets)):
	# 		if tickets[i] == 0:
	# 			continue
	# 		tickets[i] -= 1
	# 		ans += 1
	# 		if tickets[k] == 0:
	# 			return ans

	## Using Circular Queue
	# q = CircularQueue(len(tickets))
	# ans = 0
	
	# # populate queue
	# for i in range(len(tickets)):
	# 	q.append(tickets[i])

	# while True:
	# 	for i in range(len(tickets)):
	# 		nxt = q.serve()
	# 		if nxt > 0:
	# 			nxt -= 1
	# 			ans += 1
	# 		if i == k and nxt == 0:
	# 			return ans
	# 		q.append(nxt)
	pass
	


if __name__ == "__main__": # for personal tests
	pass