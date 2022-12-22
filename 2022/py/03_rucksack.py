

def parse_contents():
    with open('../data/contents-ex.txt', 'r') as contents_file:
        entries = []
        for line in contents_file:
            raw_line = line.strip()
            entries.append(raw_line)
        return entries


def calc_contents():
    # split string in half i.e. each compartment
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

    # find item in both compartments
    # calculate priorities; a->z 1->26 A->Z 27->52


def calc_sol():
    t_data = calc_contents()
    print(t_data)


if __name__ == "__main__":
    calc_sol()