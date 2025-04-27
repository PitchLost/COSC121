'''
Write a program that reads two integers from input and prints their 
ratio to 3 decimal digits, as shown in the example below. The 
two prompt strings are Top?  and Bottom?  (each with a space on the end) 
and the printed ratio is top divided by bottom. 
'''

def main():
    '''Function to get a fraction from input and divide it'''
    num_top = float(input('Top? '))
    num_bottom = float(input('Bottom? '))
    result = num_top / num_bottom
    print(f"{result:.3f}")


main()