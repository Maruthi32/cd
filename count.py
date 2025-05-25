def count_lines_spaces_tabs(filename):
    lines = 0
    spaces = 0
    tabs = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                lines += 1
                spaces += line.count(' ')
                tabs += line.count('\t')

        print(f"Total Lines : {lines}")
        print(f"Total Spaces: {spaces}")
        print(f"Total Tabs  : {tabs}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Input file name
input_file = "input.txt"  # Make sure this file exists in the same directory
count_lines_spaces_tabs(input_file)
