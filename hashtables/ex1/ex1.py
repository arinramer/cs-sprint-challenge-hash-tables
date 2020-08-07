def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # mylist = {}
    # count = 0
    # for i in weights:
    #     mylist[i] = count
    #     count += 1
    # for i in mylist.keys():
    #     num = limit - i
    #     if num in mylist.keys():
    #         print(mylist[num], mylist[i])
    #         return mylist[num], mylist[i]

    mydict = {}
    for i in range(length):
        foo = limit - weights[i]
        if foo in mydict:
            p = mydict[foo]
            l = (i, p)
            return l
        else:
            mydict[weights[i]] = i
    return None
