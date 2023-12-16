class Vowels:
    def vowels_count(self, string):
        string = string.replace(" ", "").lower()
        vowels = set("aeiou")
        string1 = set()
        for ch in string:
            if ch in vowels:
                string1.add(ch)
            else:
                pass
        if len(string1) == len(vowels):
            print("The given string contains all the vowels")
        else:
            print("The given string does not contain all the vowels")

string = input("Enter the string: ")
obj = Vowels()
obj.vowels_count(string)
