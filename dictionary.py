def poorhash(x):
    return hash(x) % 10

def insert(key, value, D, hasher=hash):
    to_insert = (hasher(key), key, value)
    D.append(to_insert)
    D.sort(key=lambda x: x[0])

def get(key, D, hasher=hash):
    index = _binary_search(D, hasher(key), 0, len(D) - 1)
    if index == -1:
        raise KeyError('Key not found in dictionary')
    return D[index][2]

def pop(key, D, hasher=hash):
    index = _binary_search(D, hasher(key), 0, len(D) - 1)
    if index == -1:
        raise KeyError('Key not found in dictionary')
    return D.pop(index)

def keys(D):
    return [x[1] for x in D]

def values(D):
    return [x[2] for x in D]

def items(D):
    return [(x[1], x[2]) for x in D]

def _binary_search(D, hash, start, end):
    if end < start:
        return -1

    mid = start + ((end - start) // 2)

    if D[mid][0] == hash:
        return mid
    elif D[mid][0] > hash:
        return _binary_search(D, hash, start, mid - 1)
    else:
        return _binary_search(D, hash, mid + 1, end)

if __name__ == "__main__":
    dictionary = []
    insert('a key', 100, dictionary)
    insert('another key', 101, dictionary)
    insert(678, 'value', dictionary)

    print(dictionary)

    print(get('a key', dictionary))
    print(get('another key', dictionary))
    print(get(678, dictionary))

    print(pop('a key', dictionary))
    print(pop(678, dictionary))

    print(dictionary)

    print(keys(dictionary))
    print(values(dictionary))
    print(items(dictionary))