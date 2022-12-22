

def parse_contents():
    with open('../data/contents.txt', 'r') as contents_file:
        groups = []
        group = []
        for line in contents_file:
            group.append(line.strip())
            if len(group) == 3:
                groups.append(group)
                group = []
        return groups


def find_badge():
    t_data = parse_contents()
    intersect = []
    for i in t_data:
        i0 = set(i[0])
        i1 = set(i[1])
        i2 = set(i[2])
        x = i0.intersection(i1, i2)
        intersect.append(x)

    p_intersects = []
    for k in intersect:
        for char in k:
            p_intersects.append(char)
    return p_intersects

def calc_priority():
    t_data = find_badge()
    char_dict = {chr(i): i - 96 for i in range(97, 123)}
    char_dict.update({chr(i): i - 38 for i in range(65, 91)})
    int_list = [char_dict[char] for char in t_data]
    return sum(int_list)


def calc_sol():
    sol = calc_priority()
    print(sol)


if __name__ == "__main__":
    calc_sol()
