import re

def specific_char(string):
    if re.search(r'^[a-z|A-Z|0-9]+$', string):
        return True
    else:
        return False

# For testing
# print(specific_char('Add: 1 + 23'))
# print(specific_char('Add123'))