'''Docstring'''
def n_halves(n):
    '''Docstrig'''
    count = 0
    while n > 1:
        n /= 2
        count += 1
    return count

ans = n_halves(17)
print(ans)