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
