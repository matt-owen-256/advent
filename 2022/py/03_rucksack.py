

def parse_contents():
    with open('../data/contents.txt', 'r') as contents_file:
        entries = []
        for line in contents_file:
            raw_line = line.strip()
            entries.append(raw_line)
        return entries


def calc_contents():
    r_data = parse_contents()
    p_data = []
    for item in r_data:
        i_len = len(item)
        t_len = i_len // 2
        substr_0 = item[:t_len]
        substr_1 = item[t_len:]
        i = [substr_0, substr_1]
        p_data.append(i)
    return p_data


def find_dup():
    t_data = calc_contents()
    dups = []
    for j in t_data:
        j0 = set(j[0])
        j1 = set(j[1])
        x = j0.intersection(j1)
        dups.append(x)

    p_dups = []
    for k in dups:
        for char in k:
            p_dups.append(char)
    return(p_dups)


def calc_priority():
    t_data = find_dup()
    char_dict = {chr(i): i - 96 for i in range(97, 123)}
    char_dict.update({chr(i): i - 38 for i in range(65, 91)})
    int_list = [char_dict[char] for char in t_data]
    return sum(int_list)


def calc_sol():
    sol = calc_priority()
    print(sol)


if __name__ == "__main__":
    calc_sol()
