def palindrome(string):
    string = string.replace(" ","").lower()
    first , last = 0 , len(string)-1
    while first<last:
        if string[first]==string[last]:
            first+=1
            last-=1
        else:
            return "The string is not a palindrome"
    return "The string is a plaindrome"

string = input("Enter the string:")
print(palindrome(string))