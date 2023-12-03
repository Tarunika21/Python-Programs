def frequency_of_element(array):
    frequency = {}
    for i in array:
        if i  in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency

n = int(input("Enter the number of elements:"))
list = []
for i in range(n):
    ele=int(input())
    list.append(ele)
result = frequency_of_element(list)
for element, count in result.items():
    print(f'Element {element} occurs {count} times.')