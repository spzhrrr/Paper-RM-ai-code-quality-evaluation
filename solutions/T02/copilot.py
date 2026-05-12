def reverse_string(s):
    reversed_str = ''
    index = len(s) - 1
    while index >= 0:
        reversed_str += s[index]
        index -= 1
    return reversed_str
