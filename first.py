grammar = {
    'E': [['T', 'E1']],
    'E1': [['+', 'T', 'E1']],
    'T': [['F', 'T1']],
    'T1': [['*', 'F', 'T1']],
    'F': [['(', 'E', ')'], ['id']]
}

firsts = {}
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

for nt in grammar: first(nt)

print("FIRST:")
for k in grammar: print(k, ':', firsts[k])
