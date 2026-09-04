s = input("Enter line: ").strip()

if s.startswith("//"):
    print("The given line is a comment.")
elif s.startswith("/*") and s.endswith("*/"):
    print("The given line is a comment.")
else:
    print("The given line is not a comment.")

print("Name: Supriya Devkota \n Roll No: 19 \n Lab No: 5")        