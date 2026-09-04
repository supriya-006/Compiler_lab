s = input("Enter string: ")
state = 0

for c in s:
    if state == 0:
        state = 1 if c == "a" else 0
    elif state == 1:
        state = 2 if c == "b" else (1 if c == "a" else 0)
    else:
        state = 1 if c == "a" else 0

print("Accepted" if state == 2 else "Rejected")
print("Name: Supriya Devkota \n Roll No.:19")