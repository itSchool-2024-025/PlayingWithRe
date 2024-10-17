import re
# Take a look at https://regexr.com/

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    input_string = "I love PyCharmPyCharm"
    pattern = r"PyCharm"
    print(re.search(pattern, input_string))


if __name__ == '__main__':
    print_hi('PyCharm')


