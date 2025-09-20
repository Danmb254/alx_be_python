#elif

purchase_amount = float(input("How much is your purchase amount?:"))

if purchase_amount >= 1000:
    discount = purchase_amount* 0.1
elif purchase_amount >= 500:
    discount = purchase_amount* 0.05
else :
    discount = 0

final_amount = purchase_amount - discount
print("Your final amount is :$" + str(final_amount))
