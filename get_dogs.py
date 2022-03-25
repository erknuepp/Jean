def get_dogs(filename):
    res_dict = {}
    with open(filename) as fh:
        for line in fh:
            if res_dict[line[0]] == None:
                res_dict[line[0]] = [line]
            else:
                temp = res_dict[line[0]]
                temp.append(line)
                res_dict[line[0]] = temp
    return res_dict

dogs = get_dogs('dogs.txt')
print(dogs)