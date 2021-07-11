def sum_of_multiples(limit, multiples):
    multiples = [multiple for multiple in multiples if multiple > 0]
    multiples_under_limit = []
    for i in range(limit):
        if any([True for base in multiples if i % base == 0]):
            multiples_under_limit.append(i)
    return sum(multiples_under_limit)
