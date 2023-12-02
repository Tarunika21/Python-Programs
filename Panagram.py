def isPanagram(string):
    string = string.replace(" ","").lower()
    unique_char = set()
    for ch in string:
        if 'a' <= ch <= 'z':
            unique_char.add(ch)
    return len(unique_char) == 26
    
string=input("Enter the string :")

if isPanagram(string):
    print(f'The given string {string} is Panagram.')
else:
    print(f'The given string {string} is not Panagram.')