'''
Write a function print_bump(size) that takes an integer parameter size and prints a 
line of stars in a bump shape of that size, as shown in the examples below. 

The bump size is the length of the longest output line, which consists of size - 1 
spaces and a single asterisk character, '*'.
'''

def print_bump(size): 
    counter = 0
    hit_max = False
    while True: 
        if counter == size -1:
            hit_max = True

        if hit_max:
            counter -= 1

        else: 
            counter += 1
        
        if hit_max and counter == 0:
            break
        
        
        print(f"{' ' * counter}*")

print_bump(5)