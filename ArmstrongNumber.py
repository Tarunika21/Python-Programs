class ArmstrongNumber:
    def is_armstrongNumber(self, number):
        length = len(str(number))
        total = 0
        temp = number

        while temp > 0:
            digit = temp % 10
            total += digit ** length
            temp //= 10

        return total == number

number = int(input("Enter the number: "))
obj = ArmstrongNumber()
if obj.is_armstrongNumber(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
