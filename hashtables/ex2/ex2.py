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


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]
reconstruct_trip(tickets, 3)
expected = ["PDX", "DCA", "NONE"]
