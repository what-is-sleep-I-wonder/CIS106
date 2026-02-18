# The input to the problem is quantity of widgets. Your program should determine the price to charge based on the schedule below. Calculate the extended price (quantity x price). Calculate tax at 7%.
# Display the extended price, tax amount and total.
# Quantity		Price
# >10000		$10
# 5000 to 10000	$20
# Below 5000	$30

tax = 0.07
quantity = int(input("Enter the quantity of widgets: "))
if quantity > 10000:
    price = 10
elif quantity >= 5000:
    price = 20
else:    price = 30
extended_price = quantity * price
tax_amount = extended_price * tax
total = extended_price + tax_amount
print(f"Extended Price: ${extended_price:.2f}")
print(f"Tax Amount: ${tax_amount:.2f}")
print(f"Total: ${total:.2f}")

# Enter a part number and quantity Determine the cost per unit using the table below. Then calculate the total cost (quantity x unit cost).  Display the part number, cost per unit and total cost.
# Note: Part number can be an integer but it can also be a string because you are not doing arithmetic on it.
# However, in your code if statement be sure to compare using consistency, that is, if item == “10” when item is a string and if item == 10 when item is an integer.
# Part Number	Cost per Unit
# 10 or 55       1.00
# 99             2.00
# 80 or 70       3.00
# All Others     5.00

part_number = input("Enter the part number: ")
quantity = int(input("Enter the quantity: "))
if part_number == "10" or part_number == "55":
    cost_per_unit = 1.00
elif part_number == "99":
    cost_per_unit = 2.00
elif part_number == "80" or part_number == "70":
    cost_per_unit = 3.00
else:    cost_per_unit = 5.00
total_cost = quantity * cost_per_unit
print(f"Part Number: {part_number}")
print(f"Cost per Unit: ${cost_per_unit:.2f}")
print(f"Total Cost: ${total_cost:.2f}")

# Enter a principle amount of a CD and year to maturity of CD. Determine the interest rate based on the amount of the principle and maturity (see below).
# Calculate first year interest (principle x interest rate). Display principle, interest rate and the interest amount for first year.
# Principle Amount	Year to Maturity	Interest Rate
# >$100000              5                   6%
# $50000 to $100000     10                  5%
# $50000 to $100000     5                   4%
# Any other amount      Any Year            2%

principle = float(input("Enter the principle amount of the CD: "))
maturity_years = int(input("Enter the year to maturity of the CD: "))
if principle > 100000 and maturity_years == 5:
    interest_rate = 0.06
elif 50000 <= principle <= 100000 and maturity_years == 10:
    interest_rate = 0.05
elif 50000 <= principle <= 100000 and maturity_years == 5:
    interest_rate = 0.04
else:    interest_rate = 0.02
first_year_interest = principle * interest_rate
print(f"Principle: ${principle:.2f}")
print(f"Interest Rate: {interest_rate * 100:.2f}%")
print(f"First Year Interest: ${first_year_interest:.2f}")

# Have the user to enter number of concert tickets. The price per ticket depends on the volume (see below).
# Display the number of tickets, price per ticket and the total cost (number of tickets x Price Per Ticket).
# Number of Tickets	Price Per Ticket
# >=25			    $50
# 10 to 24		    $60
# 5 to 9			$70
# Less 5			$75

tickets = int(input("Enter the number of concert tickets: "))
if tickets >= 25:
    price_per_ticket = 50
elif 10 <= tickets < 25:
    price_per_ticket = 60
elif 5 <= tickets < 10:
    price_per_ticket = 70
else:    price_per_ticket = 75
total_cost = tickets * price_per_ticket
print(f"Number of Tickets: {tickets}")
print(f"Price per Ticket: ${price_per_ticket:.2f}")
print(f"Total Cost: ${total_cost:.2f}")

# The user will enter employee last name, salary and job level (as noted below). Use the job level to determine the bonus rate.
# Then compute bonus to be salary times bonus rate. Display employee last name and bonus.
# Job Level	Bonus Rate
# >=10       25%
# 5 to 9     20%
# Below 5    10%

last_name = input("Enter the employee's last name: ")
salary = float(input("Enter the employee's salary: "))
job_level = int(input("Enter the employee's job level: "))
if job_level >= 10:
    bonus_rate = 0.25
elif 5 <= job_level < 10:
    bonus_rate = 0.20
else:    bonus_rate = 0.10
bonus = salary * bonus_rate
print(f"Employee Last Name: {last_name}")
print(f"Bonus: ${bonus:.2f}")