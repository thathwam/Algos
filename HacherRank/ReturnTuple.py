"""
Refer safari online notes from effective Python book....

The first way is to split the return value into a two-tuple. The first part of the tuple indicates that the operation was a success or failure. The second part is the actual result that was computed.

The point is that it's better to send exception than none. Then why not send the default exception?
"""

def divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e


def sort_priority2(numbers, group):
    found = False
    def helper(x):
        if x in group:
            found = True  # Seems simple
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)
