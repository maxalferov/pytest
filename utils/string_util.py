# return false if string not contain digits
def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)
