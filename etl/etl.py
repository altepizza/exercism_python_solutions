def transform(legacy_data):
    return {
        letter.lower(): score
        for score in legacy_data for letter in legacy_data[score]
    }
