'''
Write a function bargain_price(price, discount_percent) that returns the given price after 
discounting it by the given percentage. For example, if the price is $200 and the discount 
is 10%, the discounted price is 200×(1−10/100)=180
'''

def bargain_price(price, discount_percent):
    '''Simple 1 liner'''
    return price - price / 100 * discount_percent

new_price = bargain_price(200.0, 10.0)
print(f"{new_price:.2f}")