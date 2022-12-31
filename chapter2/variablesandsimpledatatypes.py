# Various string formatting methods

name = "ada lovelace"

# Capitalise first letter of each word
print(name.title())
# Change all characters to upper case
print(name.upper())
# Change all characters to lower case
print(name.lower())

# Example of f strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

# Removing leading whitespace
funky_str = "  hello right whitespace"
right_whitespace_str = "hello  "
print(funky_str)
print(funky_str.lstrip())
print(right_whitespace_str.rstrip())

# Remove whitespace from string
another_funky_str = "h e l l o"
print(another_funky_str)
print(another_funky_str.replace(" ", ""))

# Large numbers can be allocated using underscore to ease reading
large_num = 8_000_000
print(large_num)

# Multiple assignments can be done in a single line
x, y, z = 6, 7, 8
print(f'{x}, {y}, {z}')

# A constant is like a variable whose value stays the same throughout the program

MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)

