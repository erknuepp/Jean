import re


def check(string):
    result = False
    # return true if only contains (a-z)(A-C)(0-5) and false otherwise

    if re.match(r'^[a-z|A-C|0-5]', string):
        result = True
    else:
        result = False

    return result


print(check("Calm"))
print(check("Dan89"))
