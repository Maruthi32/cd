import re

code = "x=5+3*2 "

def lexical_analysis(code):
    tokens = re.findall(r'[a-zA-Z_]\w*|==|<=|>=|!=|[0-9]+|[+\-*/=()]', code)
    print("1. Lexical Analysis (Tokens):", tokens)
    return tokens

def syntax_analysis(tokens):
    if tokens[1] != '=':
        raise SyntaxError("Expected '=' after identifier")
    print("\n2. Syntax Analysis (Parse Tree):")
    print("  Assignment")
    print("  |── Identifier:", tokens[0])
    print("  └── Expression:", ' '.join(tokens[2:]))
    return ('assign', tokens[0], tokens[2:])

def semantic_analysis(ast):
    _, var, expr = ast
    for token in expr:
        if re.match(r'[a-zA-Z_]\w*', token) and token != var:
            raise NameError(f"Undeclared variable '{token}'")
    print("\n3. Semantic Analysis: PASSED")
    return True

def intermediate_code(expr):
    temp = 1
    var, expr = expr.split('=')
    tokens, i = [], 0
    intermediate = []

    while i < len(expr):
        if expr[i] in '+-*/':
            tokens.append(expr[i])
            i += 1
        elif expr[i].isalnum():
            start = i
            while i < len(expr) and expr[i].isalnum():
                i += 1
            tokens.append(expr[start:i])
        else:
            i += 1  

    for ops in ('*/', '+-'):
        i = 0
        while i < len(tokens):
            if tokens[i] in ops:
                intermediate.append(f"t{temp} = {tokens[i-1]} {tokens[i]} {tokens[i+1]}")
                tokens[i-1:i+2] = [f"t{temp}"]
                temp += 1
                i = 0
            else:
                i += 1
    intermediate.append(f"{var.strip()} = {tokens[0]}")
    print("\n4. Intermediate Code:")
    for line in intermediate:
        print(" ", line)
    return intermediate

def code_optimization(intermediate):
    optimized = []
    for line in intermediate:
        parts = line.split(' = ')
        if len(parts) == 2:
            dest, expr = parts
            try:
                result = eval(expr)
                optimized.append(f"{dest} = {result}")
            except:
                optimized.append(line)
    print("\n5. Code Optimization:")
    for line in optimized:
        print(" ", line)
    return optimized

def generate_assembly(optimized_code):
    print("\n6. Code Optimization:")
    for line in optimized_code:
        lhs, rhs = line.split('=')
        lhs = lhs.strip()
        rhs = rhs.strip()
        tokens = rhs.split()
        if len(tokens) == 3:
            op = tokens[1]
            if op == '+':
                instruction = "ADD"
            elif op == '-':
                instruction = "SUB"
            elif op == '*':
                instruction = "MUL"
            elif op == '/':
                instruction = "DIV"
            else:
                instruction = "UNKNOWN"

            print(f"MOV R1, {tokens[0]}")
            print(f"{instruction} R1, {tokens[2]}")
            print(f"MOV {lhs}, R1")
        else:
            print(f"MOV {lhs}, {rhs}")

tokens = lexical_analysis(code)
ast = syntax_analysis(tokens)
semantic_analysis(ast)
intermediate = intermediate_code(code)
optimized = code_optimization(intermediate)
generate_assembly(optimized)
