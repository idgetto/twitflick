def avg(lst):
    return sum(lst) / len(lst)

def remap(val, old_min, old_max, new_min, new_max):
    rel_val = val - old_min
    old_range = old_max - old_min
    percent = float(rel_val) / old_range

    new_range = new_max - new_min
    new_rel_val = percent * new_range
    new_val = new_rel_val + new_min

    return new_val
