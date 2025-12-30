amount = int(input("enter amount:"))

if amount < 4000:
    amount -= (10*amount)/100

elif amount < 10000:
    amount -= (20*amount)/100

else:
    amount -= (30*amount)/100


print(amount)