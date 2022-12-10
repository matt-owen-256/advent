

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
    indexed_sums = [(s, index) for index, s in t_data.items()]
    sorted_sums = sorted(indexed_sums, key=lambda x: x[0], reverse=True)
    t3 = sorted_sums[:3]
    total = sum([x[0] for x in t3])
    sol = t3, total
    print(sol)


if __name__ == "__main__":
    calc_sol()
