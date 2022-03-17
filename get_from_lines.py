def get_from_lines(file):
    res_list = []
    with open(file) as fh:
        for line in fh:
            line.rstrip()
            if line.find("From:") >= 0:
                res_list.append(line)
    return res_list


lines = get_from_lines("mbox_short.txt")
print(lines[0])
