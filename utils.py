def avg(lst):
    """ finds the average of a list
    >>> avg([1, 2, 3, 4, 5])
    3.0
    >>> avg([1])
    1.0
    >>> avg([])
    0.0
    """

    if not lst:
        return 0.0
    return float(sum(lst)) / len(lst)

def remap(val, old_min, old_max, new_min, new_max):
    """ remaps values from one scale to another
    >>> remap(3, 1, 3, 1, 10)
    10.0
    >>> remap(0, 0, 1, 4, 100)
    4.0
    >>> remap(2, 1, 3, 0, 100)
    50.0
    """

    rel_val = val - old_min
    old_range = old_max - old_min
    percent = float(rel_val) / old_range

    new_range = new_max - new_min
    new_rel_val = percent * new_range
    new_val = new_rel_val + new_min

    return new_val

if __name__ == "__main__":
    import doctest
    doctest.testmod()
