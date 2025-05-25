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
intermediate_code("a=b*c+d+e")
