def add(x, y):
    """Add function"""
    return x + y


def subtract(x, y):
    """subtract function"""
    return x - y


def multiply(x, y):
    """ multiply function"""
    return x * y


def divide(x, y):
    """divide function """
    if y == 0:
        raise ValueError('Cannot divide by 0')
    return x / y
