

def parse_inv():
    with open('../data/inventory.txt', 'r') as inv_file:
        entries = [[]]
        for line in inv_file:
            raw_line = line.strip()
            if not raw_line:
                entries.append([])
            else:
                entries[-1].append(raw_line)
    return entries


def index_inv():
    inv_data = parse_inv()
    indexed_data = {}
    for i, sublist in enumerate(inv_data):
        indexed_data[i] = sum(map(int, sublist))
    return indexed_data


def calc_sol():
    t_data = index_inv()
    max_cals = max(t_data.values())
    max_index = [k for k, v in t_data.items() if v == max_cals]
    sol = max_index, max_cals
    print(sol)


if __name__ == "__main__":
    calc_sol()
