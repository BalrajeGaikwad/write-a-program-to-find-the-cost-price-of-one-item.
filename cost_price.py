#If the total selling price of 15 items and the total profit earned on them is input through the keyboard, write a program to find the cost price of one item.

selling_price=int(input("Enter the selling price :-"))
total_profit=int(input("Enter the total profit"))


cost_price=selling_price-total_profit

cost_per_item=cost_price/15

print("Cost price per item is - ",cost_per_item)