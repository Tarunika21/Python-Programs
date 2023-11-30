def Fibonacci(term):
    if term<0:
        print("Invalid input")
    values = []
    first_term=0
    second_term=1
    third_term = first_term + second_term
    values.append(first_term)
    values.append(second_term)
    for i in range(2,term+1):
        values.append(third_term)
        first_term = second_term
        second_term = third_term
        third_term = first_term + second_term
    return values

n = int(input("Enter the number of terms:"))
result= Fibonacci(n)
print(result)
    
