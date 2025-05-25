def peephole_optimize(code_lines):
    optimized = []
    for line in code_lines:
        parts = line.strip().split()
        if len(parts) == 3:
            op, arg1, arg2 = parts[0], parts[1].rstrip(','), parts[2]
            if op == "MOV" and arg1 == arg2:
                continue 
            if op == "ADD" and arg2 == "0":
                continue  
            if op == "MUL" and arg2 == "1":
                continue 
        optimized.append(line)
    return optimized

code = [
    "MOV A, A",
    "ADD A, 0",
    "MUL B, 1",
    "MOV C, D",
    "SUB A, 2"
]

optimized_code = peephole_optimize(code)

print("\n".join(optimized_code))
