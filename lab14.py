table = {
    ("E", "i"): ["T", "Q"], ("E", "("): ["T", "Q"],
    ("Q", "+"): ["+", "T", "Q"], ("Q", ")"): [], ("Q", "$"): [],
    ("T", "i"): ["F", "R"], ("T", "("): ["F", "R"],
    ("R", "+"): [], ("R", "*"): ["*", "F", "R"], ("R", ")"): [], ("R", "$"): [],
    ("F", "i"): ["i"], ("F", "("): ["(", "E", ")"],
}

input_string = input("Enter expression using i, +, *, (, ): ").replace(" ", "") + "$"
stack = ["$", "E"]
index = 0
accepted = True

while stack:
    top = stack.pop()
    token = input_string[index]
    if top == "$":
        accepted = token == "$"
        break
    if top == token:
        index += 1
    elif top in "EQTRF":
        production = table.get((top, token))
        if production is None:
            accepted = False
            break
        stack.extend(reversed(production))
    else:
        accepted = False
        break

print("Accepted" if accepted else "Rejected")
print("Name: Supriya Devkota \n Roll No: 19 \n Lab No: 14")
