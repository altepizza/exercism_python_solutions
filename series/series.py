def slices(series, length):
    slices = []
    if length <= len(series) and length > 0:
        for i in range(len(series)):
            if i + length <= len(series):
                slices.append(series[i:i+length])
    if slices:
        return slices
    raise ValueError('ASDF')
