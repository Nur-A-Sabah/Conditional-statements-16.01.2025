ap = int(input("Enter the Actual price of the product: "))
sp = int(input("Enter the Selling price of the product: "))

if sp > ap:
    profit = sp - ap
    print(f"Apnar Profit : {profit}")
else:
    loss = ap - sp
    print(f"Apnar loss : {loss}")