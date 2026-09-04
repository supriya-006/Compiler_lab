tokens = input("Enter expression using i, +, *, (, ): ").replace(" ", "") + "$"
stack = []
i = 0

while True:
    reduced = True
    while reduced:
        reduced = False
        lookahead = tokens[i]
        reductions = [
            (["i"], "F", set("+*)$")),
            (["(", "E", ")"], "F", set("+*)$")),
            (["T", "*", "F"], "T", set("+)$")),
            (["F"], "T", set("+*)$")),
            (["E", "+", "T"], "E", set("+)$")),
            (["T"], "E", set("+)$")),
        ]
        for handle, result, valid_lookaheads in reductions:
            if stack[-len(handle):] == handle and lookahead in valid_lookaheads:
                stack[-len(handle):] = [result]
                print("Reduce:", " ".join(handle), "->", result)
                reduced = True
                break

    if stack == ["E"] and tokens[i] == "$":
        print("Accepted")
        break
    if tokens[i] == "$":
        print("Rejected")
        break

    if tokens[i] in "i+*()":
        stack.append(tokens[i])
        print("Shift:", tokens[i])
        i += 1
    else:
        print("Rejected")
        break

print("Name: Supriya Devkota \n Roll No: 19 \n Lab No: 11")
