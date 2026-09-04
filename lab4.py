s = input("Enter string: ")
i = 0

while i < len(s) and s[i] == "a":
    i += 1

start = i
while i < len(s) and s[i] == "b":
    i += 1

print("Accepted" if start < i and i == len(s) else "Rejected")
print("Name: Supriya Devkota \n Roll No: 19 \n Lab No: 4")  
