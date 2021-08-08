import math


def largest_product(series, size):
    if size == 0 and len(series) == 0:
        return 1
    if size < 0:
        raise ValueError('size needs to be > 0')
    int_list = [int(x) for x in series]
    products = []
    for idx, n in enumerate(int_list):
        if idx + size <= len(int_list):
            products.append(math.prod(int_list[idx:idx+size]))
    return max(products)
