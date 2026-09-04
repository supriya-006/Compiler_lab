# Compiler Lab

## Lab 1: Prefixes, Suffixes and Substrings

```python
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
```

## Lab 2: Identifier and Keyword

```python
keywords = ["if", "else", "for", "while", "def", "class", "return", "int", "float", "True", "False"]
word = input("Enter word: ")

if word in keywords:
	print("Keyword")
elif word[0].isalpha() or word[0] == "_":
	valid = True
	for c in word:
		if not (c.isalnum() or c == "_"):
			valid = False
	print("Identifier" if valid else "Invalid")
else:
	print("Invalid")

print("Name: Supriya Devkota \n Roll No: 19 \n Lab No: 2")
```

## Lab 3: Implementation of DFA

```python
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
```

## Lab 4: Implementation of Regular Expression

```python
s = input("Enter string: ")
i = 0

while i < len(s) and s[i] == "a":
	i += 1

start = i
while i < len(s) and s[i] == "b":
	i += 1

print("Accepted" if start < i and i == len(s) else "Rejected")
print("Name: Supriya Devkota \n Roll No: 19 \n Lab No: 4")
```

## Lab 5: Comment in C

```python
s = input("Enter line: ").strip()

if s.startswith("//"):
	print("The given line is a comment.")
elif s.startswith("/*") and s.endswith("*/"):
	print("The given line is a comment.")
else:
	print("The given line is not a comment.")

print("Name: Supriya Devkota \n Roll No: 19 \n Lab No: 5")
```

## Lab 6: Computation of FIRST

```python
g = {"E": ["aT", "b"], "T": ["c", "d"]}
first = {}

for nt in g:
	first[nt] = set()
	for p in g[nt]:
		x = p[0]
		if x not in g:
			first[nt].add(x)
		else:
			first[nt] |= first[x]

for nt in first:
	print("FIRST(" + nt + ") =", first[nt])
print("Name: Supriya Devkota \n Roll No: 19 \n Lab No: 6")
```

## Lab 7: Computation of FOLLOW

```python
g = {"E": ["T+F", "F"], "T": ["i"], "F": ["i"]}
follow = {"E": {"$"}, "T": set(), "F": set()}

for a in g:
	for p in g[a]:
		for i in range(len(p) - 1):
			if p[i] in g and p[i+1] not in g:
				follow[p[i]].add(p[i+1])

for x in follow:
	print("FOLLOW(" + x + ") =", follow[x])

print("Name: Supriya Devkota \n Roll No: 19 \n Lab No: 7")
```

## Lab 8: Identifier Validation

```python
import re

identifier = input("Enter identifier: ")

if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", identifier):
	print("Valid identifier")
else:
	print("Invalid identifier")

print("Name: Supriya Devkota \n Roll No: 19 \n Lab No: 8")
```

## Lab 9: Lexical Analysis

```python
import re

code = input("Enter statement: ")
keywords = {"int", "float", "char", "if", "else", "while", "return"}
pattern = r"[A-Za-z_][A-Za-z0-9_]*|\d+(?:\.\d+)?|==|!=|<=|>=|[+\-*/%=<>();{},]"

tokens = re.findall(pattern, code)

for token in tokens:
	if token in keywords:
		category = "Keyword"
	elif re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", token):
		category = "Identifier"
	elif re.fullmatch(r"\d+(?:\.\d+)?", token):
		category = "Number"
	else:
		category = "Operator/Symbol"
	print(token, "->", category)

print("Name: Supriya Devkota \n Roll No: 19 \n Lab No: 9")
```

## Lab 10: Type Checking

```python
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
```

## Lab 11: Shift-Reduce Parser

```python
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
```

## Lab 12: Implementation of Symbol Table

```python
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
```

## Lab 13: Implementation of SLR(1) Grammar

```python
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
```

## Lab 14: Implementation of LL(1) Grammar

```python
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
```

## Lab 15: Implementation of Brute-Force Parser

```python
def parse_expression(text):
	position = 0

	def match(symbol):
		nonlocal position
		if position < len(text) and text[position] == symbol:
			position += 1
			return True
		return False

	def expression():
		if not term():
			return False
		while match("+"):
			if not term():
				return False
		return True

	def term():
		if not factor():
			return False
		while match("*"):
			if not factor():
				return False
		return True

	def factor():
		if match("i"):
			return True
		if match("("):
			if expression() and match(")"):
				return True
		return False

	return expression() and position == len(text)

expression = input("Enter expression using i, +, *, (, ): ").replace(" ", "")
print("Accepted" if parse_expression(expression) else "Rejected")
print("Name: Supriya Devkota \n Roll No: 19 \n Lab No: 15")
```
