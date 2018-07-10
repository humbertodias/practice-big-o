# https://www.interviewcake.com/question/python/product-of-other-numbers

numbers = [1, 7, 3, 4]

def get_products_of_ints_except_at_index(numbers, index):
	product = 1 # 1
	# O(n)
	for idx in range(0, len(numbers)):
		if idx != index:
			number = numbers[idx]
			# Avoiding null product
			if numbers[idx] == 0: 
				number = 1 
			product *= number
	return product


def get_products_of_all_ints_except_at_index(numbers):
	length = len(numbers) #1
	product = [ 1 for x in range(length)] # n
	for idx in range(length): # n
		product[idx] = get_products_of_ints_except_at_index(numbers, idx)
	return product

print(get_products_of_all_ints_except_at_index(numbers))