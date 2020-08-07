def has_negatives(a):
    """
    YOUR CODE HERE
    """
    mylist = {}
    result = []
    for i in a:
        num = abs(i)
        if num in mylist:
            mylist[num] += 1
        else:
            mylist[num] = 1
    for i in mylist:
        if mylist[i] > 1:
            result.append(i)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
