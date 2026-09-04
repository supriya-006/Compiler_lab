import re

identifier = input("Enter identifier: ")

if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", identifier):
    print("Valid identifier")
else:
    print("Invalid identifier")

print("Name: Supriya Devkota \n Roll No: 19 \n Lab No: 8")
