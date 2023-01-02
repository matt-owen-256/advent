

def parse_start():
    with open('../data/start-ex.txt', 'r') as start_file:
        lines = []
        for line in start_file:
            p_line = [line[i:i+4] for i in range(0, len(line), 4)]
            lines.append(p_line)
        return lines


# def parse_proc():
#     with open('../data/proc-ex.txt', 'r') as proc_file:


def calc_grid():
    t = parse_start()
    return t


def calc_sol():
    sol = calc_grid()
    for item in sol:
        print(item)


if __name__ == "__main__":
    calc_sol()
