

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
    d_lst = ['RR', 'PP', 'SS']

    score_map = {
        'R': 1,
        'P': 2,
        'S': 3
    }

    t_data = calc_strat()
    score = 0
    for item in t_data:
        if item[1] in score_map:
            score += score_map[item[1]]
        if item in w_lst:
            score += 6
        if item in d_lst:
            score += 3
    return score


def calc_sol():
    print(calc_score())
    

if __name__ == "__main__":
    calc_sol()
