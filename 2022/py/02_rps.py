

def parse_strat():
    with open('../data/strategy.txt', 'r') as strat_file:
        entries = []
        for line in strat_file:
            raw_line = line.strip()
            entries.append(raw_line)
        return entries


def calc_strat():
    r_data = parse_strat()
    p_data = []
    for item in r_data:
        item = item.replace(' ', '')
        ttab = str.maketrans('ABCXYZ', 'RPSRPS')
        item = item.translate(ttab)
        p_data.append(item)
    return p_data


def calc_score():
    w_lst = ['SR', 'RP', 'PS']
    l_lst = ['RS', 'PR', 'SP']
    d_lst = ['RR', 'PP', 'SS']

    t_data = calc_strat()

    score = 0
    for item in t_data:
        if item[1] == 'R':
            score += 1
        if item[1] == 'P':
            score += 2
        if item[1] == 'S':
            score += 3
        if item in w_lst:
            score += 6
        if item in l_lst:
            score += 0
        if item in d_lst:
            score += 3
    return score


def calc_sol():
    print(calc_score())


if __name__ == "__main__":
    calc_sol()
