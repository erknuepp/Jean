import re

def match_add(string):
    if re.search(r'Add: [1-9] [\+] [1-9]{2}$', string):
        return True
    else:
        return False

print(match_add('Add: 1 + 23'))
print(match_add('Add: 2 + 259'))
print(match_add('Add: 21 + 23'))
print(match_add('Add: 1 + 23'))