def binarySearch(array,target):
    low,high = 0,len(array)-1
    while low<=high:
        mid = (low+high)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            high = mid-1
        else:
            low = mid+1
    return -1

n = int(input("Enter the number of elements:"))
array = []
print("Enter the elements:")
for i in range(n):
    element = int(input())
    array.append(element)
target = int(input("Enter the element to search:"))
result = binarySearch(array,target)
if result != -1:
    print(f'The element is found in the index {result}.')
else:
    print('The element is not found.')
        