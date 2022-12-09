

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
    max_cals = max(p_data.values())
    max_index = [k for k, v in p_data.items() if v == max_cals]
    return max_index, max_cals


def run_seq():
    print(calc())


if __name__ == "__main__":
    run_seq()
