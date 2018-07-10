numbers = [5,8,6,1]
'''
5-8 -3
8-6 2
6-1 6

8-5 3
8-6 2
8-1 7

6-5 1
5-8 -3
6-1 5
'''

# O(n^2)
def get_greatest_difference(numbers):
	greatest_diff = 0 
	for num1 in numbers: # O(n)
		for num2 in numbers: # O(n)
			diff = num1 - num2
			if diff > greatest_diff :
				greatest_diff = diff
	return greatest_diff

def get_greatest_differencev2(nums):
  sorted_nums = sorted(nums)
  return sorted_nums[-1] - sorted_nums[0]

def get_greatest_differencev3(nums):
  max = nums[0]
  min = nums[0]
  # O(n)
  for num in nums:
    if num > max:
      max = num
    elif num < min:
      min = num
  return max - min

print(get_greatest_difference(numbers))

print(get_greatest_differencev2(numbers))

print(get_greatest_differencev3(numbers))