# your code goes here
def sumTo(arr,k):
	hashTable = set()
	for v in arr:
		if (k-v) not in hashTable:
			hashTable.add(v)
		else:
			return True
	return False

assert not sumTo([10,15,3,7],90)
assert sumTo([7,15,3,10],17)
assert not sumTo([10,15,3,4],17)