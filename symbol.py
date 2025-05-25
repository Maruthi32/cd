def create_symbol_table():
    return {}

def insert_symbol(table, name, type_, scope, value=None):
    if name in table:
        print(f"Symbol '{name}' already exists.")
    else:
        table[name] = {
            'name': name,
            'type': type_,
            'scope': scope,
            'value': value,
            'address': id(value)
        }
        print(f"Inserted symbol '{name}'.")

def lookup_symbol(table, name):
    return table.get(name, None)

def delete_symbol(table, name):
    if name in table:
        del table[name]
        print(f"Deleted symbol '{name}'.")
    else:
        print(f"Symbol '{name}' not found.")

def update_symbol(table, name, type_=None, scope=None, value=None):
    if name in table:
        if type_ is not None:
            table[name]['type'] = type_
        if scope is not None:
            table[name]['scope'] = scope
        if value is not None:
            table[name]['value'] = value
            table[name]['address'] = id(value)
        print(f"Updated symbol '{name}'.")
    else:
        print(f"Symbol '{name}' not found for update.")

def display_table(table):
    print("\nSymbol Table:")
    print("Name\tType\tScope\tValue\tAddress")
    print("-" * 40)
    for symbol in table.values():
        print(f"{symbol['name']}\t{symbol['type']}\t{symbol['scope']}\t{symbol['value']}\tAddress: {symbol['address']}")

symbol_table = create_symbol_table()

insert_symbol(symbol_table, "x", "int", "global", 10)
insert_symbol(symbol_table, "y", "float", "local", 3.14)
insert_symbol(symbol_table, "z", "string", "global", "hello")

display_table(symbol_table)

print("\nLookup 'y':", lookup_symbol(symbol_table, "y"))

delete_symbol(symbol_table, "y")

display_table(symbol_table)

print("\nUpdating 'x'...")
update_symbol(symbol_table, "x", value=20, scope="local")

display_table(symbol_table)
