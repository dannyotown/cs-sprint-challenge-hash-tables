def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    for arr in arrays:
        for item in arr:
            if item not in d:
                d[item] = 1
            else:
                d[item] += 1

    result = [key for key in d if d[key] == len(arrays)]
    return result


if __name__ == "__main__":
    arrays = [[1, 2, 3],
              [1, 4, 5, 3]]
    print(intersection(arrays))
