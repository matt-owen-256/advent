

def parse_strat():
    with open('../data/assignments-ex.txt', 'r') as assign_file:
        assigns = []
        for line in assign_file:
            raw_line = line.strip()
            assigns.append(raw_line)
        return assigns
