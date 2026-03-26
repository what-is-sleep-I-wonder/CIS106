# Allow the user to enter quantities and prices in a loop. Use a function to compute the total (quantity times price). The function should be passed the quantity and price and then return the total.
# In the function, provide a 10% discount if the total is over $10,000.00.  Display quantity, price and total. Sum and display the total extended price.
def totalFunc(quantity, price):
    total = quantity * price
    if total > 10000:
        total = total * 0.9
    return total

print("Would you like to enter a quantity and price?")
var_continue = input()
totalExtendedPrice = 0
while var_continue == "Yes":
    print("Enter quantity")
    quantity = int(input())
    print("Enter price")
    price = float(input())
    print("Calculating...")
    totalFunc(quantity, price)
    total = totalFunc(quantity, price)
    print(f"Quantity: {quantity}")
    print(f"Price: {price}")
    print(f"Total: {total:.2f}")
    totalExtendedPrice = totalExtendedPrice + total
    print("Enter another item and price?")
    var_continue = input()
print(f"Total extended price: {totalExtendedPrice:.2f}")

# Enter players last name, number of hits and at bats at the keyboard. Use a function to compute batting average. Pass the hits and at bats to the function.
# The function should return batting average. Display last name and batting average.  Give a count of the number of players entered.
def battingAverageFunc(hits, atBats):
    battingAverage = hits / atBats
    return battingAverage

print("Would you like to enter a player's stats?")
var_continue = input()
playerCount = 0
while var_continue == "Yes":
    print("Enter the player's last name")
    lastName = input()
    print("Enter the number of hits")
    hits = int(input())
    print("Enter the number of at bats")
    atBats = int(input())
    print("Calculating...")
    battingAverageFunc(hits, atBats)
    battingAverage = battingAverageFunc(hits, atBats)
    print(lastName)
    print(f"{battingAverage:.3f}")
    playerCount = playerCount + 1
    print("Enter another player's stats?")
    var_continue = input()
print(f"Number of players entered: {playerCount}")

# Prompt the user to repeatedly to do the program input (Yes or No)). If they respond Yes, go into the loop and prompt them for last name, month and sales.
# Write a function to compute next month’s forecast. Pass to the function month and sales. Determine the forecast percent (see below) and compute next month’s sales to be sales x (1+forecast percent).
# Return next month’s sales and display the value.

#Month			Forecast Percent
#Jan, Feb, Mar			0.10
#Apr, May, Jun			0.15
#Jul, Aug, Sep			0.20
#Oct, Nov, Dec			0.25

def forecastFunc(month, sales):
    if month == "Jan" or month == "Feb" or month == "Mar":
        forecastPercent = 0.10
    elif month == "Apr" or month == "May" or month == "Jun":
        forecastPercent = 0.15
    elif month == "Jul" or month == "Aug" or month == "Sep":
        forecastPercent = 0.20
    elif month == "Oct" or month == "Nov" or month == "Dec":
        forecastPercent = 0.25
    nextMonthSales = sales * (1 + forecastPercent)
    return nextMonthSales

print("Would you like to enter a sales forecast?")
var_continue = input()
while var_continue == "Yes":
    print("Enter the last name")
    lastName = input()
    print("Enter the month")
    month = input()
    print("Enter the sales")
    sales = float(input())
    print("Calculating...")
    forecastFunc(month, sales)
    nextMonthSales = forecastFunc(month, sales)
    print(lastName)
    print(f"Next month's sales: {nextMonthSales:.2f}")
    print("Enter another sales forecast?")
    var_continue = input()

# Prompt the user to repeatedly to do the program (input (Yes or No)). If they response Yes go into the loop and prompt the user for make, model, electric vehicle code (Y or N) and MSRP (sticker price) of an
# automobile. Write a function to compute the out the door price. Pass to the function the MSRP, make, model and electric vehicle code. Determine the percent off the MSRP then compute the new MSRP and finally add 7%
# sales tax to the total. Return and display the total. Also sum all MSRP’s and sum of all sales price of the cars (MSRP – discount + tax).

#To determine percent off MSRP			Percent off MSRP
#Honda Accord					          0.10
#Toyota Rav4					          0.15
#All electric vehicles				      0.30
#All other vehicles				          0.05

def outTheDoorFunc(MSRP, make, model, electricVehicleCode):
    if make == "Honda" and model == "Accord":
        percentOffMSRP = 0.10
    elif make == "Toyota" and model == "Rav4":
        percentOffMSRP = 0.15
    elif electricVehicleCode == "Y":
        percentOffMSRP = 0.30
    else:
        percentOffMSRP = 0.05
    newMSRP = MSRP * (1 - percentOffMSRP)
    total = newMSRP * 1.07
    return total

print("Would you like to enter a car's information?")
var_continue = input()
totalMSRP = 0
totalSalesPrice = 0
while var_continue == "Yes":
    print("Enter the make")
    make = input()
    print("Enter the model")
    model = input()
    print("Is it an electric vehicle? (Y or N)")
    electricVehicleCode = input()
    print("Enter the MSRP")
    MSRP = float(input())
    print("Calculating...")
    outTheDoorFunc(MSRP, make, model, electricVehicleCode)
    total = outTheDoorFunc(MSRP, make, model, electricVehicleCode)
    print(f"Total: {total:.2f}")
    totalMSRP = totalMSRP + MSRP
    totalSalesPrice = totalSalesPrice + total
    print("Enter another car's information?")
    var_continue = input()
print(f"Total MSRP: {totalMSRP:.2f}")
print(f"Total Sales Price: {totalSalesPrice:.2f}")

# The input consists of quantity, price and discount rate. Use a function to compute the discount amount and discounted price. Then, display these values in the main part of the program,
# along with the quantity and price. (The function should return both discount amount and discounted price).

def discountFunc(quantity, price, discountRate):
    discountAmount = quantity * price * discountRate
    discountedPrice = quantity * price - discountAmount
    return discountAmount, discountedPrice
print("Would you like to calculate a discount?")
var_continue = input()
while var_continue == "Yes":
    print("Enter quantity")
    quantity = int(input())
    print("Enter price")
    price = float(input())
    print("Enter discount rate (as a decimal)")
    discountRate = float(input())
    print("Calculating...")
    discountFunc(quantity, price, discountRate)
    discountAmount, discountedPrice = discountFunc(quantity, price, discountRate)
    print(f"Quantity: {quantity}")
    print(f"Price: {price}")
    print(f"Discount Amount: {discountAmount:.2f}")
    print(f"Discounted Price: {discountedPrice:.2f}")
    print("Calculate another discount?")
    var_continue = input()

# Enter the student’s last name and 3 exam scores. Use a function to compute the average and total points.
# This function should return both total points and average. Display student’s last name, total points and average exam score.
def examFunc(score1, score2, score3):
    totalPoints = score1 + score2 + score3
    average = totalPoints / 3
    return totalPoints, average
print("Would you like to enter a student's exam scores?")
var_continue = input()
while var_continue == "Yes":
    print("Enter the student's last name")
    lastName = input()
    print("Enter exam score 1")
    score1 = float(input())
    print("Enter exam score 2")
    score2 = float(input())
    print("Enter exam score 3")
    score3 = float(input())
    print("Calculating...")
    examFunc(score1, score2, score3)
    totalPoints, average = examFunc(score1, score2, score3)
    print(lastName)
    print(f"Total Points: {totalPoints:.2f}")
    print(f"Average Exam Score: {average:.2f}")
    print("Enter another student's exam scores?")
    var_continue = input()