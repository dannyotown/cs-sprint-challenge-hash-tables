#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __str__(self):
        return f'source: {self.source}, destination: {self.destination}'


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    d = {}
    arr = []
    for ticket in tickets:
        d[ticket.source] = ticket.destination
    arr.insert(0, d['NONE'])
    count = 0
    while len(arr) < length:
        arr.append(d[arr[count]])
        count += 1
    return arr
