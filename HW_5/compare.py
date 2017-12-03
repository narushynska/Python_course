from utils import measure_time

MAX_ITER = 100000
LST = range(0, MAX_ITER)


@measure_time
def while_loop_iter():
    i = 0
    res = []
    while i < MAX_ITER:
        res.append(LST[i])
        i += 1
    return res


@measure_time
def for_loop_iter():
    res = []
    for temp in LST:
        res.append(temp)
    return res


@measure_time
def list_comprehension():
    return [item for item in LST]


@measure_time
def dict_comprehension():
    return {item: item for item in LST}


@measure_time
def set_comprehension():
    return {item for item in LST}


@measure_time
def func_generator():
    return list(item for item in LST)


if __name__ == '__main__':
    while_loop_iter()
    for_loop_iter()
    list_comprehension()
    dict_comprehension()
    set_comprehension()
    func_generator()
