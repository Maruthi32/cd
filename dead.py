# def constant_folding(expr):
#     return eval(expr) if all(c.isdigit() or c in "+-*/ " for c in expr) else expr

# print(constant_folding("3 + 5 * 2"))  # Output: 13


# def strength_reduction(expr):
#     return expr.replace("* 2", "+ x").replace("x * 2", "x + x").replace('x**2','x*x')

# print(strength_reduction("x =  x**2"))  
def dead_code_elimination(code):
    lines = code.split("\n")
    used_vars = set()
    result = []
    for line in lines[::-1]:
        if "=" in line:
            var, expr = line.split("=")
            if var.strip() in used_vars or not used_vars:
                used_vars.update(expr.strip().split())
                result.append(line)
        else:
            used_vars.update(line.strip().split())
            result.append(line)
    return "\n".join(result[::-1])

print(dead_code_elimination("a = c\nd = c * b + 6\ns = a * b"))
