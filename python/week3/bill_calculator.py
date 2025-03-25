price = int(input("Enter the total of your bill: "))
discount_percent = int(input("Enter your discount percentage: "))

def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent/100))
        return discounted_price
    else:
        return price

print(f"Total bill price: {calculate_discount(price, discount_percent)}")