def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Length of strands differs')
    distance = [a for a, b in zip (strand_a, strand_b) if a != b]
    return len(distance)
