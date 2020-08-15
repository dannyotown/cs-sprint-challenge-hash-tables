def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # first pass
    # s = set()
    # for i in range(len(a)):
    #     for j in range(len(a)):
    #         if a[i] + a[j] == 0:
    #             s.add(abs(a[i]))
    # return list(s)
    d = {}
    arr = []
    for num in a:
        if num < 0 and abs(num) not in d:
            abso = abs(num)
            d[abso] = 1
        elif num < 0 and abs(num) in d:
            d[abs(num)] += 1
        elif num > 0 and num not in d:
            d[num] = 1
        elif num > 0 and num in d:
            d[num] += 1

    for key, value in d.items():
        if value == 2:
            arr.append(key)
    return arr


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
