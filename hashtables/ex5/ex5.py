# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    hashmap = dict(zip(queries, files))
    result = []
    for i in files:
        if i in hashmap:
            hashmap[i].append(i)
        else:
            hashmap[i] = []
            hashmap[i].append(i)
    print(result)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
