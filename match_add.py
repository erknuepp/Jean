import re

def match_add(string):
    if re.search(r'Add: [0-9]{1} [\+] [1-9]{2}$', string):
        return string
    else:
        return "This string does not match."

# For testing uncomment code
# print(match_add('Add: 1 + 23'))
# print(match_add('Add: 9 + 51'))
# print(match_add('Add: 0 + 89'))
# print(match_add('Add: 4 + 5'))
# print(match_add('Add: 4 + 5'))
# print(match_add('Add: 67 + 89'))
# print(match_add('Add: 1 + 234'))
# print(match_add('Add: 1 - 23'))
# print(match_add('Add: 3 + 678'))