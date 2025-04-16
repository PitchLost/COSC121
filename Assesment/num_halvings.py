'''
Write a function num_halvings(num) that takes an int parameter and 
returns how many divisions are required to get to zero.
'''

def num_halvings(num):
    '''Nearly just fried my comp with an inf loop!'''
    division_counter = 0
    our_number = num
    while True: 
        if our_number == 0: 
            return division_counter
        our_number = int(our_number / 2)
        division_counter += 1

print(num_halvings(0))
print(num_halvings(43))
print(num_halvings(1))