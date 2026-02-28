# Allow the user to enter a principal amount and interest rate. Repeatedly (need a loop to control the program execution) compute the annual interest (principle x rate).
# Compute ending balance to be principal (beginning balance + interest). Display year, beginning balance and ending balance for each of the first 5 years. Display the accumulated interest for the 5 years.
# Note:  the new balance by year, this will be the principle for the following year.
year = 1
principal = float(input("Enter the principal amount: "))
interestRate = int(input("Enter the interest rate (as a percentage): "))
interestPercent = float(interestRate) / 100
while year <= 5:
    annualInterest = principal * interestPercent
    endingBalance = principal + annualInterest
    print("Year: ", year, "Beginning Balance: ", principal, "Ending Balance: ", endingBalance)
    principal = endingBalance
    year = year + 1

# 2. Fibonacci sequence is a sequence of natural order. The sequence is: 1, 1, 2, 3, 5, 8 etc. where it is a series of numbers that may start with 0 and 1, and each subsequent number is the sum of the
# two preceding numbers. For this exercise, start with 1.Use a for loop compute and display first 20 numbers in the sequence.
first = 1
second = 1
print(first)
print(second)
for i in range(3, 21):
    next = first + second
    print(next)
    first = second
    second = next

# Create a text file that contains employee last name and salary. Read in this data. Determine the bonus rate based on the chart below. Use that rate to compute bonus.
# For each line display the employee’s last name, salary and bonus. After the loop display the sum of all bonuses paid out.
totalBonuses = 0.0
fileName = "M8P3 Text File.txt"
infile = open(fileName, 'r')
nextLine = infile.readline()
while not nextLine == '':
    lastName = nextLine
    nextLine = infile.readline()
    salary = float(nextLine)
    nextLine = infile.readline()
    if salary >= 100000:
        bonus = 0.2
    else:
        if 50000 <= salary:
            bonus = 0.15
        else:
            bonus = 0.1
    bonusAmount = salary * bonus
    totalBonuses = totalBonuses + bonusAmount
    print(lastName, f"{salary:,.2f}", f"{bonusAmount:,.2f}")
print(totalBonuses)

# Create a text file with item, quantity and price. Read through the file one line at a time. Compute the extended price (quantity x price). For each line display the item, quantity, price and extended price.
# After the loop display the sum of all the extended prices, the count of the number of orders and the average order.
numOrders = 0
totalPrices = 0.0
fileName = "M8P4 Text File.txt"
infile = open(fileName, 'r')
nextLine = infile.readline()
while not nextLine == '':
    numOrders = numOrders + 1
    itemName = nextLine
    nextLine = infile.readline()
    quantity = int(nextLine)
    nextLine = infile.readline()
    itemPrice = float(nextLine)
    nextLine = infile.readline()
    extendedPrice = quantity * itemPrice
    print(itemName, quantity, f"{itemPrice:,.2f}", f"{extendedPrice:,.2f}")
    totalPrices = totalPrices + extendedPrice
averageOrderPrice = totalPrices / numOrders
print(numOrders)
print(f"{averageOrderPrice:,.2f}")

# Create a text file with student last name, district code (I or O) and number of credits taken. Compute tuition owed (credits taken x cost per credit).
# Cost per credit for in district students (district code I) is 250.00. Out of district students pay 500.00 per credit. For each line display student last name, credits taken and tuition owed.
# After the loop display sum of all tuition owed and the number of students.
totalTuition = 0
numStudents = 0
infile = open("M8P5 Text File.txt", 'r')
nextLine = infile.readline()
while not nextLine == '':
    numStudents = numStudents + 1
    lastName = nextLine
    nextLine = infile.readline()
    code = nextLine
    nextLine = infile.readline()
    creditHours = int(nextLine)
    nextLine = infile.readline()
    if code == "I":
        costPer = 250.0
    else:
        costPer = 500.0
    tuitionOwed = creditHours * costPer
    print(lastName, creditHours, f"{tuitionOwed:,.2f}")
    totalTuition = totalTuition + tuitionOwed
print(f"{totalTuition:,.2f}")
print(numStudents)