def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = {}
    newlist = []

    for i in arrays:
        for x in i:
            if x in result:
                result[x] += 1
            else:
                result[x] = 1
    for n in result:
        if result[n] == len(arrays):
            newlist.append(n)
            
            

    return newlist


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
