

def parse_strat():
    with open('../data/assignments.txt', 'r') as assign_file:
        assigns = []
        for line in assign_file:
            raw_line = line.strip()
            p_line = raw_line.replace(',', '-').split('-') 
            p2_line = [int(item) for item in p_line]
            assigns.append(p2_line)
        return assigns


def calc_sol():
    t_data = parse_strat()
    count = 0
    for item in t_data:
        t0 = set(range(item[0], item[1]+1))
        t1 = set(range(item[2], item[3]+1))
        if t0.intersection(t1):
            count += 1
    sol = count
    print(sol)


if __name__ == "__main__":
    calc_sol()
