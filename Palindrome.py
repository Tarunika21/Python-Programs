def palindrome(string):
    string=string.replace(" ","").lower()
    if string == string[::-1]:
        return("The given string is a palindrome.")
    else:
        return("The given string is not a palindrome.")

string = input("Enter the string:")
print(palindrome(string))