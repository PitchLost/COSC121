'''Rewrite this function to use a while loop'''

def wonky(items):
    '''Crazy this works'''
    thingy = []
    i = -3
    prev = 0

    idx = 0
    while idx < len(items):

        i += 1
        if i >= 0:
            thingy.append(items[idx] * i - prev)
        else:
            thingy.append(items[idx] - 2 * i * prev)
        prev = items[idx]

        idx += 1
    return thingy

print(wonky([3, -5, 1, 0, 5]))


# def wonky_old(items):
#     """Do some weird calculations with a list items, computing a new list
#        to be returned.
#     """
#     thingy = []
#     i = -3
#     prev = 0
#     for item in items:
#         i += 1
#         if i >= 0:
#             thingy.append(item * i - prev)
#         else:
#             thingy.append(item - 2 * i * prev)
#         prev = item
#     return thingy