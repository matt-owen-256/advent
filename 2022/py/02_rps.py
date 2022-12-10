

def parse_strat():
    with open('../data/strategy-ex.txt', 'r') as strat_file:
        entries = [[]]
        for line in strat_file:
            raw_line = line.strip()
            entries[-1].append(raw_line)
        return entries


def calc_sol():
    print(parse_strat())


if __name__ == "__main__":
    calc_sol()
