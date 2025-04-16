'''
Write a function last3back(data) that takes a list data as a parameter and
 returns a list consisting of the last three items of data in reverse order.  

You may assume data contains at least 3 items.
'''

def last3back(data):
    '''There is so a better way of doing this for sure'''
    return data[::-1][:3]


print(last3back([0,1,2,3,4]))
print(last3back([10,20,30]))