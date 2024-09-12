import sys

def ft_filter(function, iterable):
    """
    Custom implementation of Python's filter() function.
    It filters elements of iterable for which the function returns True.
    """
    return [item for item in iterable if function(item)]
