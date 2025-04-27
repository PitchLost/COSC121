'''
Write a function print_reciprocals(nums) that takes a list of 
integers as a parameter. For each integer in the list the function 
prints a line displaying the reciprocal of that number in the form

1/8 = 0.1250

where there is a single space on each side of the equals sign and 
the reciprocal is always displayed to 4 decimal places.

Notes: 

The reciprocal of a number is 1 over than number.
The function does not return anything.
'''

def print_reciprocals(nums):
    '''Clean function'''
    for num in nums:
        print(f"1/{num} = {1 / int(num):.4f}")