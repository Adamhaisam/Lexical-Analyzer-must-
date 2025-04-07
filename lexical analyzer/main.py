def is_letter(char):
    return char.isalpha() or char == '_'

def is_digit(char):
    return char.isdigit()

def lexer(code):
    keywords = {"if", "else", "elif", "while", "for"}
    reserved = {"int"}

    i = 0
    length = len(code)
    tokens = []

    while i < length:
        char = code[i]

        # Skip whitespace
        if char in ' \t\n':
            i += 1
            continue

        # Identifiers, Keywords, and Reserved Words
        if is_letter(char):
            start = i
            while i < length and (is_letter(code[i]) or is_digit(code[i])):
                i += 1
            word = code[start:i]
            if word in reserved:
                tokens.append("RESERVED_WORD")
            elif word in keywords:
                tokens.append("KEYWORD")
            else:
                tokens.append("IDENTIFIER")

        # Numbers
        elif is_digit(char):
            start = i
            while i < length and is_digit(code[i]):
                i += 1
            tokens.append("INT_LITERAL")

        # String Literals
        elif char == '"':
            i += 1
            start = i
            while i < length and code[i] != '"':
                i += 1
            if i < length:
                tokens.append("STRING_LITERAL")
                i += 1  # Skip closing quote
            else:
                tokens.append("ERROR")  # Unterminated string

        # Multi-char operators
        elif char in ['!', '=', '<', '>']:
            next_char = code[i + 1] if i + 1 < length else ''
            if next_char == '=':
                tokens.append("OPERATOR")
                i += 2
            else:
                tokens.append("OPERATOR")
                i += 1

        # Arithmetic operators
        elif char == '+':
            tokens.append("PLUS_OP")
            i += 1
        elif char == '-':
            tokens.append("SUB_OP")
            i += 1
        elif char == '*':
            tokens.append("MULT_OP")
            i += 1
        elif char == '/':
            tokens.append("DIV_OP")
            i += 1

        # Assignment operator
        elif char == '=':
            tokens.append("ASSIGN_OP")
            i += 1

        # Semicolon
        elif char == ';':
            tokens.append("SEMICOLON")
            i += 1

        # Parentheses
        elif char == '(':
            tokens.append("LPAREN")
            i += 1
        elif char == ')':
            tokens.append("RPAREN")
            i += 1

        # Unknown characters
        else:
            tokens.append("UNKNOWN")
            i += 1

    # Print all tokens on one line
    print(' '.join(tokens))


# Example usage
if __name__ == "__main__":
    user_input = input("Enter code: ")
    lexer(user_input)
