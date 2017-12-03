from utils import measure_time

MAX_ITER = 100000
LST = range(0, MAX_ITER)


@measure_time
def while_loop_iter(degree):
    i = 0
    res = []
    while i < MAX_ITER:
        res.append(LST[i]**degree)
        i += 1
    return res


@measure_time
def for_loop_iter(degree):
    res = []
    for temp in LST:
        res.append(temp**degree)
    return res


@measure_time
def list_comprehension(degree):
    return [item**degree for item in LST]


@measure_time
def dict_comprehension(degree):
    return {item: item**degree for item in LST}


@measure_time
def set_comprehension(degree):
    return {item**degree for item in LST}


@measure_time
def func_generator(degree):
    return list(item**degree for item in LST)


if __name__ == '__main__':
    while_loop_iter(2)
    for_loop_iter(2)
    list_comprehension(2)
    dict_comprehension(2)
    set_comprehension(2)
    func_generator(2)
