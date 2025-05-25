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

optimized =['t1 = 6', 't2 = 5 + t1', 'x = t2']
generate_assembly(optimized)
