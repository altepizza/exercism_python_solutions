def flatten(iterable):
    tmp = []
    for i in iterable:
        if type(i) is list:
            tmp.extend(flatten(i))
        elif i is not None:
            tmp.append(i)
    return tmp
