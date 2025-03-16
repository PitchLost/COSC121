'''
The following function crashes if it is given certain integer numbers a and b.
 Find the cause of the crash and give values of a and b such that the crash occurs.
'''

def trouble(a, b):
    z = 12317952
    x = z - a
    y = z - b
    x += 361
    (x, y) = (y, x)
    print(x, y)
    if x >= y:
        print('x >= y')
        z = x - y
    else:
        z = x // y
    z = z * y
    return z

print(trouble(12318313, 12317953))