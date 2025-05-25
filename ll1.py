grammar = {
    'E': [['T', 'E1']],
    'E1': [['+', 'T', 'E1']],
    'T': [['F', 'T1']],
    'T1': [['*', 'F', 'T1']],
    'F': [['(', 'E', ')'], ['id']]
}

firsts, follows = {}, {}
start = 'E'

def first(X):
    if X not in grammar: return {X}
    if X in firsts: return firsts[X]
    firsts[X] = set()
    for prod in grammar[X]:
        for sym in prod:
            f = first(sym)
            firsts[X] |= f - {'ε'}
            if 'ε' not in f: break
        else: firsts[X].add('ε')
    return firsts[X]

def follow(X):
    if X in follows: return follows[X]
    follows[X] = {'$'} if X == start else set()
    for A in grammar:
        for prod in grammar[A]:
            for i in range(len(prod)):
                if prod[i] == X:
                    beta = prod[i+1:]
                    if beta:
                        f = set()
                        for sym in beta:
                            f |= first(sym) - {'ε'}
                            if 'ε' not in first(sym): break
                        else: f |= follow(A)
                        follows[X] |= f
                    elif A != X:
                        follows[X] |= follow(A)
    return follows[X]

for nt in grammar: first(nt)
for nt in grammar: follow(nt)

print("FIRST:")
for k in grammar: print(k, ':', firsts[k])
print("\nFOLLOW:")
for k in grammar: print(k, ':', follows[k])
table = {nt: {} for nt in grammar}
for nt in grammar:
    for prod in grammar[nt]:
        for t in first(prod[0]):
            table[nt][t] = prod

print("\nLL(1) Parsing Table:")
for nt in table:
    for t in table[nt]:
        print(f"M[{nt}][{t}] = {table[nt][t]}")
