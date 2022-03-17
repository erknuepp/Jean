import re


def get_year_counts(lines):
    year_dict = dict()
    i: str
    for i in lines:
        dates = i.split(' ')
        for d in dates:
            year = re.split(r'[/|-]', d)[2]
            if year_dict.get(year) == None:
                year_dict.setdefault(year, 1)
            else:
                year_dict[year] = year_dict[year] + 1
    new_list = [(k, v) for k, v in year_dict.items()]
    new_list.sort(key=lambda y: y[1])
    return new_list


lines = ["02/04/20 12-30-19", "03/04/20", "08-20-18"]
print(get_year_counts(lines))
