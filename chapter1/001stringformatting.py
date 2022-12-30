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
print(funky_str)
print(funky_str.lstrip())

# Remove whitespace from string
another_funky_str = "h e l l o"
print(another_funky_str)
print(another_funky_str.replace(" ", ""))
