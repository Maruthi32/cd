import re

keywords = {"if", "else", "while", "return", "int", "float"}
operators = {'+', '-', '*', '/', '=', '==', '!=', '<', '>', '<=', '>='}
delimiters = {';', ',', '(', ')', '{', '}'}

def classify_token(token):
    if token in keywords:
        return "Keyword"
    elif token in operators:
        return "Operator"
    elif token in delimiters:
        return "Delimiter"
    elif re.fullmatch(r'[0-9]+', token):
        return "Number"
    elif re.fullmatch(r'[a-zA-Z_][a-zA-Z0-9_]*', token):
        return "Identifier"
    else:
        return "Unknown"

def tokenize(code):
    tokens = re.findall(r'\w+|==|!=|<=|>=|[^\s]', code)
    for token in tokens:
        token_type = classify_token(token)
        print(f"{token:10} : {token_type}")

code = "int a = 10; if (a > 5) return a + 1;"
tokenize(code)
