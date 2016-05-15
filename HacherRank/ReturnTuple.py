"""
Refer safari online notes from effective Python book....

The first way is to split the return value into a two-tuple. The first part of the tuple indicates that the operation was a success or failure. The second part is the actual result that was computed.
"""

def divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None
