#
#   Arrange a list so that when added to a tree will cause the tree to be completely balanced
#
def make_list(lst):
    if lst == []:
        return []

    lst = sorted(lst)
    mid = len(lst) / 2

    return [lst[mid]] + make_list(lst[:mid]) + make_list(lst[mid + 1:])
