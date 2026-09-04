keywords = ["if", "else", "for", "while", "def", "class", "return", "int", "float", "True", "False"]
word = input("Enter word: ")

if word in keywords:
    print("Keyword")
elif word[0].isalpha() or word[0] == "_":
    valid = True
    for c in word:
        if not (c.isalnum() or c == "_"):
            valid = False
    print("Identifier" if valid else "Invalid")
else:
    print("Invalid")

print("Name: Supriya Devkota \n Roll No: 19 \n Lab No: 2")      