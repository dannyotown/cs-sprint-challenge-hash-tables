# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = dict()
    for path in files:
        file = path.split('/')
        file_in_path = file[-1:][0]
        if file_in_path in d:
            d[file_in_path] = d[file_in_path] + [path]
        else:
            d[file_in_path] = [path]
    arr = []
    for value in queries:
        if value in d:
            arr = arr + d[value]
    return arr


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
