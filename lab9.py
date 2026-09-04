import re

code = input("Enter statement: ")
keywords = {"int", "float", "char", "if", "else", "while", "return"}
pattern = r"[A-Za-z_][A-Za-z0-9_]*|\d+(?:\.\d+)?|==|!=|<=|>=|[+\-*/%=<>();{},]"

tokens = re.findall(pattern, code)

for token in tokens:
    if token in keywords:
        category = "Keyword"
    elif re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", token):
        category = "Identifier"
    elif re.fullmatch(r"\d+(?:\.\d+)?", token):
        category = "Number"
    else:
        category = "Operator/Symbol"
    print(token, "->", category)

print("Name: Supriya Devkota \n Roll No: 19 \n Lab No: 9")
