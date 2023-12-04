def checkprime(n):
    if n > 1:
        for i in range(2,int(n/2)+1):
            if n%i ==0:
                return False
        else:
            return True
    return False

n = int(input("Enter the number to check:"))
if(checkprime(n)):
    print(f'{n} is a prime number.')
else:
    print(f'{n} is not a prime number.')
    