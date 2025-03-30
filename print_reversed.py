'''
Write a function print_reversed(filename) that reads a file then prints out 
the lines from the file in reversed order, i.e. the last line is written first, 
then the second to last, and so on.
'''

def print_reversed(filename):
   '''Function'''
   infile = open(filename, 'r')
   content = infile.read()

print_reversed('Tests/data.txt')