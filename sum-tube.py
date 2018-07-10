numbers = [1,2,3,9]
#numbers = [1,2,4,4]
# O(n)
def sum(numbers, sum):
	it = iter(numbers)
	for a,b in zip(it,it):
		if a+b == sum:
			return True
	return False

print (sum(numbers, 8))