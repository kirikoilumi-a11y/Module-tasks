def digitize(n):
    result = []

    for digit in str(n):
        result.insert(0, int(digit))

    return result