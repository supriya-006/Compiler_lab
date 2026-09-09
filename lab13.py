grammar = {
    "E": [["E", "+", "T"], ["t"]],
    "T": [["T", "*", "F"], ["F"]],
    "F": [["(", "E", ")"], ["a"]],
}
nonterminals = set(grammar)
productions = [("S'", ["E"])]
for head, alternatives in grammar.items():
    productions.extend((head, body) for body in alternatives)

terminals = {
    symbol
    for _, body in productions
    for symbol in body
    if symbol not in nonterminals
}

follow = {head: set() for head in nonterminals}
follow["E"].add("$")
changed = True
while changed:
    changed = False
    for head, body in productions[1:]:
        for index, symbol in enumerate(body):
            if symbol in nonterminals and index + 1 < len(body):
                next_symbol = body[index + 1]
                if next_symbol in terminals:
                    changed |= next_symbol not in follow[symbol]
                    follow[symbol].add(next_symbol)
            elif symbol in nonterminals:
                before = len(follow[symbol])
                follow[symbol] |= follow[head]
                changed |= len(follow[symbol]) != before


def closure(items):
    items = set(items)
    changed = True
    while changed:
        changed = False
        for production_index, dot in list(items):
            head, body = productions[production_index]
            if dot < len(body) and body[dot] in nonterminals:
                for index, (candidate_head, _) in enumerate(productions):
                    if candidate_head == body[dot] and (index, 0) not in items:
                        items.add((index, 0))
                        changed = True
    return frozenset(items)


def move(items, symbol):
    return closure(
        (production_index, dot + 1)
        for production_index, dot in items
        if dot < len(productions[production_index][1])
        and productions[production_index][1][dot] == symbol
    )


states = [closure({(0, 0)})]
transitions = {}
state_index = 0
while state_index < len(states):
    symbols = {
        productions[production_index][1][dot]
        for production_index, dot in states[state_index]
        if dot < len(productions[production_index][1])
    }
    for symbol in symbols:
        next_state = move(states[state_index], symbol)
        if next_state not in states:
            states.append(next_state)
        transitions[(state_index, symbol)] = states.index(next_state)
    state_index += 1

action = {}
goto = {}
for state, items in enumerate(states):
    for production_index, dot in items:
        head, body = productions[production_index]
        if dot < len(body):
            symbol = body[dot]
            next_state = transitions[(state, symbol)]
            if symbol in terminals:
                action[(state, symbol)] = ("s", next_state)
            else:
                goto[(state, symbol)] = next_state
        elif head == "S'":
            action[(state, "$")] = ("a", 0)
        else:
            for symbol in follow[head]:
                action[(state, symbol)] = ("r", production_index)

input_string = input("Enter expression using t, a, +, *, (, ): ").replace(" ", "") + "$"
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
        head, body = productions[value]
        del states[-len(body):]
        states.append(goto[(states[-1], head)])
    else:
        print("Accepted")
        break

print("Name: Supriya Devkota \n Roll No: 19 \n Lab No: 13")
