def has22(nums):
    has = False
    for n in nums:
        if int(n) == 2 and has == True:
            return True
        elif int(n) == 2:
            has = True
        else:
            has = False
    return False


print(has22([1, 2, 2]))
print(has22([1, 2, 1, 2]))
