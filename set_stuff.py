def set_stuff(a,b):
    union = a.union(b)
    subset = a.issubset(b)
    superset = a.issuperset(b)

    return union,subset,superset
