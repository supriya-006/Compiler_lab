action = {
    (0, "i"): ("s", 5), (0, "("): ("s", 4),
    (1, "+"): ("s", 6), (1, "$"): ("a", 0),
    (2, "+"): ("r", 2), (2, "*"): ("s", 7), (2, ")"): ("r", 2), (2, "$"): ("r", 2),
    (3, "+"): ("r", 4), (3, "*"): ("r", 4), (3, ")"): ("r", 4), (3, "$"): ("r", 4),
    (4, "i"): ("s", 5), (4, "("): ("s", 4),
    (5, "+"): ("r", 6), (5, "*"): ("r", 6), (5, ")"): ("r", 6), (5, "$"): ("r", 6),
    (6, "i"): ("s", 5), (6, "("): ("s", 4),
    (7, "i"): ("s", 5), (7, "("): ("s", 4),
    (8, "+"): ("s", 6), (8, ")"): ("s", 11),
    (9, "+"): ("r", 1), (9, "*"): ("s", 7), (9, ")"): ("r", 1), (9, "$"): ("r", 1),
    (10, "+"): ("r", 3), (10, "*"): ("r", 3), (10, ")"): ("r", 3), (10, "$"): ("r", 3),
    (11, "+"): ("r", 5), (11, "*"): ("r", 5), (11, ")"): ("r", 5), (11, "$"): ("r", 5),
}
goto = {(0, "E"): 1, (0, "T"): 2, (0, "F"): 3, (4, "E"): 8, (4, "T"): 2, (4, "F"): 3, (6, "T"): 9, (6, "F"): 3, (7, "F"): 10}
productions = {1: ("E", 3), 2: ("E", 1), 3: ("T", 3), 4: ("T", 1), 5: ("F", 3), 6: ("F", 1)}

input_string = input("Enter expression using i, +, *, (, ): ").replace(" ", "") + "$"
states = [0]
index = 0

while True:
    token = input_string[index]
    operation = action.get((states[-1], token))
    if operation is None:
        print("Rejected")
        break
    kind, value = operation
    if kind == "s":
        states.append(value)
        index += 1
    elif kind == "r":
        head, length = productions[value]
        del states[-length:]
        states.append(goto[(states[-1], head)])
    else:
        print("Accepted")
        break

print("Name: Supriya Devkota \n Roll No: 19 \n Lab No: 13")
