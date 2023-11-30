def dutch_flag_sort(array):
    low, mid, high = 0, 0, len(array)-1
    while mid <= high:
        if array[mid] == 0:
            array[low], array[mid] = array[mid], array[low]
            low += 1
            mid += 1
        elif array[mid] == 1:
            mid += 1
        else:
            array[mid], array[high] = array[high], array[mid]
            high -= 1

n = int(input("Enter the number of terms:"))
array = []
print("Enter the terms:")
for i in range(n):
    element = int(input())
    array.append(element)
dutch_flag_sort(array)
print(array)
