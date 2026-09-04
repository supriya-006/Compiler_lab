symbol_table = {}

count = int(input("Enter number of declarations: "))
for _ in range(count):
    data_type, identifier = input("Enter type and identifier: ").split()
    symbol_table[identifier] = data_type

search_name = input("Enter identifier to search: ")
if search_name in symbol_table:
    print(search_name, "->", symbol_table[search_name])
else:
    print("Identifier not found")

print("Symbol Table:")
for identifier, data_type in symbol_table.items():
    print(identifier, "->", data_type)

print("Name: Supriya Devkota \n Roll No: 19 \n Lab No: 12")
