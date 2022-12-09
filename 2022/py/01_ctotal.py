

def parse_inv():
    with open('../data/inventory.txt', 'r') as inv_file:
        entries = [[]]
        for line in inv_file:
            line = line.strip()
            if not line:
                entries.append([])
            else:
                entries[-1].append(line)
    return entries


def index_inv():
    inv_data = parse_inv()
    indexed_data = {}
    
    for i, sublist in enumerate(inv_data):
        indexed_data[i] = sum(map(int, sublist))
    return indexed_data


def calc():
    p_data = index_inv()
    indexed_sums = [(sum, index) for index, sum in p_data.items()]
    sorted_sums = sorted(indexed_sums, key=lambda x: x[0], reverse=True)
    t3 = sorted_sums[:3]
    total = sum([x[0] for x in t3])
    return t3, total


def run_seq():
    print(calc())


if __name__ == "__main__":
    run_seq()
