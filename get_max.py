def get_max(days):
    most =  max(set(days), key=days.count)
    if most == 'M':
        return 'Monday'
    elif most == 'T':
        return 'Tuesday'
    elif most == 'W':
        return 'Wednesday'
    elif most == 'R':
        return 'Thursday'
    elif most == 'F':
        return 'Friday'
    elif most == 'S':
        return 'Saturday'
    else:
        return 'Sunday'


print(get_max(['M', 'M', 'T']))