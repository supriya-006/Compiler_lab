s = 'aab'
print("Prefixes:")
for i in range(1, len(s) + 1):
   print(s[:i])

print("Suffixes:")
for i in range(len(s)):
   print(s[i:])

print("Substrings:")
for i in range(len(s)):
   for j in range(i + 1, len(s) + 1):
       print(s[i:j])

print("Name: Supriya Devkota \n Roll No: 19 \n Lab No: 1")       
