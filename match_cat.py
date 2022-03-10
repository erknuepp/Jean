import re

def match_cat(string):
    if re.search(r'^[Cc][Aa][Tt]$', string):
        return True
    else:
        return False

# For testing
# print(match_cat('cat'))
# print(match_cat('CAT'))
# print(match_cat('Cat'))
# print(match_cat('cAt'))
# print(match_cat('dog'))