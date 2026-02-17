#Allow a user to enter a quantity of an item.  If the quantity is greater than or equal to 1000, the unit price should be $3.00. For quantities under 1000 the unit price is $5.00.
#Compute extended price to be quantity x unit price. Compute tax to be 7% of the extended price. The total is computed as extended price plus the tax. Display the quantity, unit price, extended price, tax and total.

tax=0.07
quantity=int(input("Enter the quantity of the item: "))
if quantity >= 1000:
    unit_price=3.00
else:
    unit_price=5.00
extended_price=quantity*unit_price
tax_amount=extended_price*tax
total=extended_price+tax_amount
print("Quantity: ", quantity)
print("Unit Price: $", unit_price)
print("Extended Price: $", extended_price)
print("Tax: $", tax_amount)
print("Total: $", total)

#The program asks the user for an item and quantity. Determine the unit price of the item based on the chart below. Compute the extended price to be quantity x unit price.
#Display the item, unit price and extended price. Note: if the item entered is not A then assume the item is B. No need to check for B.

item=input("Enter the item (A or B): ")
quantity=int(input("Enter the quantity of the item: "))
if item == "A":
    unit_price=10.00
else:
    unit_price=20.00
extended_price=quantity*unit_price
print("Item: ", item)
print("Unit Price: $", unit_price)
print("Extended Price: $", extended_price)

#Enter the number of books to order and cost per book. If the order total is over $50.00 shipping is free. If the order total is $50.00 or under charge $25 shipping.
#Display the order total and shipping charge (note 0 should display for a free shipping charge)

quantity=int(input("Enter the number of books to order: "))
cost_per_book=float(input("Enter the cost per book: "))
order_total=quantity*cost_per_book
if order_total > 50.00:
    shipping_charge=0.00
else:
    shipping_charge=25.00
print("Order Total: $", order_total)
print("Shipping Charge: $", shipping_charge)

#The warranty of an appliance depends on the cost of the appliance. For appliances over $1,000 the warranty cost is 10% of the price.
#For appliances $1,000 or less the warranty cost is 5% of the price. The user will enter the name and cost of an appliance.
#Display name and cost of appliance, the cost of the warranty and the total (cost of the appliance + warranty).

appliance_name=input("Enter the name of the appliance: ")
appliance_cost=float(input("Enter the cost of the appliance: "))
if appliance_cost > 1000.00:
    warranty_cost=appliance_cost*0.10
else:
    warranty_cost=appliance_cost*0.05
total_cost=appliance_cost+warranty_cost
print("Appliance Name: ", appliance_name)
print("Cost of Appliance: $", appliance_cost)
print("Cost of Warranty: $", warranty_cost)
print("Total Cost: $", total_cost)

#Enter the user’s last name, number of dependents and gross income. Compute adjusted gross income to be gross income minus dependents times $12000.
#Next determine an income tax rate. Adjusted gross incomes over $50,000 have a tax rate of 20%. Adjusted gross incomes $50,000 or under have a tax rate of 10%.
#Once you determine the tax rate, compute income tax to be adjusted gross income times tax rate. If the income tax is less than 0, set the income tax to $100.
#Display last name, gross income, number of dependents, adjusted gross income, and income tax.

last_name=input("Enter your last name: ")
dependents=int(input("Enter the number of dependents: "))
gross_income=float(input("Enter your gross income: "))
adjusted_gross_income=gross_income-(dependents*12000)
if adjusted_gross_income > 50000.00:
    tax_rate=0.20
else:    tax_rate=0.10
income_tax=adjusted_gross_income*tax_rate
if income_tax < 0:
    income_tax=100.00
print("Last Name: ", last_name)
print("Gross Income: $", gross_income)
print("Number of Dependents: ", dependents)
print("Adjusted Gross Income: $", adjusted_gross_income)
print("Income Tax: $", income_tax)