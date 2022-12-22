

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
        ttab = str.maketrans('ABCXYZ', 'RPSLDW')
        item = item.translate(ttab)
        p_data.append(item)

    p2_data = []
    append_map = {
        'L': {'R': 'S', 'P': 'R', 'S': 'P'},
        'D': {'R': 'R', 'P': 'P', 'S': 'S'},
        'W': {'R': 'P', 'P': 'S', 'S': 'R'}
    }
    for j in p_data:
        j += append_map[j[1]][j[0]]
        p2_data.append(j)
    return p2_data


def calc_sol():
    score_map = {
        'R': 1,
        'P': 2,
        'S': 3
    }

    t_data = calc_strat()
    score = 0
    for item in t_data:
        if item[2] in score_map:
            score += score_map[item[2]]
        if item[1] == 'W':
            score += 6
        if item[1] == 'D':
            score += 3
    print(score)
    

if __name__ == "__main__":
    calc_sol()
