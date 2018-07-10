# O(n)
def sumOfNumbers(numbers):
	sum = 0
	for n in numbers:
		sum += n
	return sum

numbers = [4,3,2,1]
print(sumOfNumbers(numbers))

#O(n^2)
def bubbleSort(numbers):
	n = len(numbers) # O(1)
	for i in range(n): # O(n)
		for j in range(0, n-i-1): # O(n-i-1)
			if numbers[j] > numbers[j+1]: # O(1)
				swap(numbers, j)
# O(3)
def swap(numbers, j):
	tmp = numbers[j]
	numbers[j] = numbers[j+1]
	numbers[j+1] = tmp
	
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

print(numbers)
bubbleSort(numbers)
print(numbers)			



numbers = [4,3,2,1]
mergeSort(numbers)


numbers = [4,3,2,1]
insertionSort(numbers)
print(numbers)