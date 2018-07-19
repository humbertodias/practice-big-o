n = -123

def reverse_integer(n):
	rev = 0
	while n != 0:
		rev = rev * 10 + abs(n) % 10
		n = int(n / 10)
	return rev 

print(reverse_integer(n))