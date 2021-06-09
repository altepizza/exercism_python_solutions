def slices(series, length):
    if length <= len(series) and length > 0:
        return [series[i:i+length] for i in range(len(series)) if i + length <= len(series)]
    raise ValueError('ASDF')
