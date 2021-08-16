def transform(legacy_data):
    data = {}
    for score in legacy_data:
        for letter in legacy_data[score]:
            data[letter.lower()] = score
    return data
