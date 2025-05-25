def cse(code):
    expr_map = {}
    result = []
    for line in code.split("\n"):
        if "=" in line:
            var, expr = line.split("=")
            expr = expr.strip()
            if expr in expr_map:
                result.append(f"{var.strip()} = {expr_map[expr]}")
            else:
                expr_map[expr] = var.strip()
                result.append(line)
    return "\n".join(result)

print(cse("a = b + c\nd = b + c\nc = b + c + d + s"))
