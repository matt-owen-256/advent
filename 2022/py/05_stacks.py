

def parse_start():
    with open('../data/start-ex.txt', 'r') as start_file:
        grid = []
        col = []
        for line in start_file:
            if len(col) <= 4:
                l_str = str(line)
                p_str = l_str.replace(l_str[3], '', 1)
                col.append(p_str)
                grid.append(col)
                col = []
        return grid


# def parse_proc():
#     with open('../data/proc-ex.txt', 'r') as proc_file:


def calc_grid():
    g = parse_start()
    return g


def calc_sol():
    sol = calc_grid()
    for item in sol:
        print(item)


if __name__ == "__main__":
    calc_sol()
