def primenumbers(m,n):
    prime = []
    for i in range(m,n):
        if i == 0 or i==1:
            continue
        for j in range(2, int(i/2)+1):
            if i%j ==0:
                break
        else:
            prime.append(i)
    return prime

m = int(input("Enter the starting range:"))
n = int(input("Enter the ending range: "))
lst = primenumbers(m,n)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)