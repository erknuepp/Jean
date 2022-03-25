def get_min(days):
    most =  min(set(days), key=days.count)
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


print(get_min(['M', 'M', 'T']))