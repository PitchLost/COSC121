'''Write a function print_cumulatives(numbers) that takes a non-empty 
list of integers numbers as a parameter and prints a series of partial 
sums in the format shown in the table below. The first line of output 
shows just the first number, the second shows the first number plus 
the second, the third shows the sum of the first three numbers, and 
so on.
'''

def print_cumulatives(numbers):
    '''Yep'''
    buffer = 0
    for i, num in enumerate(numbers):
        buffer += num
        print(f"Sum up to i = {i}: {buffer}")
         
print_cumulatives([333])