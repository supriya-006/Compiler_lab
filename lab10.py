import re

statement = input("Enter declaration (for example, int x = 10): ").strip()
pattern = r"(int|float|char)\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.+)"
match = re.fullmatch(pattern, statement)

if not match:
    print("Invalid declaration")
else:
    data_type, identifier, value = match.groups()
    value = value.strip()

    if data_type == "int":
        valid = re.fullmatch(r"[+-]?\d+", value) is not None
    elif data_type == "float":
        valid = re.fullmatch(r"[+-]?(?:\d+\.\d+|\d+)", value) is not None
    else:
        valid = re.fullmatch(r"'.'", value) is not None

    if valid:
        print("Type checking successful")
    else:
        print("Type error: value does not match", data_type)

print("Name: Supriya Devkota \n Roll No: 19 \n Lab No: 10")
