# Five programs for Module 3

#1  Allow the user to enter the stock ticker symbol (ie MSFT for Microsoft), number of shares and cost per share.
#   Compute and display amount invested to be number of shares times cost per share. 

tickerSym = input("Enter the stock ticker symbol: ")
numShares = int(input("Enter the number of shares: "))
costPerShare = float(input("Enter the cost per share: "))
amountInvested = numShares * costPerShare
print(f"Amount invested in {tickerSym}: ${amountInvested:.2f}")

#2  The student will enter their last name, midterm and final exam scores (0 – 100 points). Compute the total exam
#   points to be the sum of 40% of midterm and 60% of the final exam.  Display student last name and total exam points.

LastName = input("Enter your last name: ")
MidtermScore = float(input("Enter your midterm exam score (0-100): "))
FinalExamScore = float(input("Enter your final exam score (0-100): "))
print(f"Student Last Name: {LastName}")
TotalExamPoints = (0.4 * MidtermScore) + (0.6 * FinalExamScore)
print(f"Total Exam Points: {TotalExamPoints:.2f}")

#3  You and two friends completed a job and received an amount that is entered into the problem. You are to split the
#   amount received evenly between the three of you. Compute and display what each of you will receive.

TotalAmount = float(input("Enter the total amount received for the job: "))
AmountPerPerson = TotalAmount / 3
print(f"Amount each person receives: ${AmountPerPerson:.2f}")

#4  Enter the make, model, msrp amount and discount percent of an auto you are interested in. Compute the amount off
#   msrp you will receive as well as the discounted price. The amount off is computed to be the msrp times the discount
#   percent (you can enter as a decimal so no need to divide by 100). The discounted price is the msrp minus the amount off.
#   Display the make, model, mrsp, discount percent, amount off and discounted price.

Make = input("Enter the make of the auto: ")
Model = input("Enter the model of the auto: ")
MSRP = float(input("Enter the MSRP amount: "))
DiscountPercent = float(input("Enter the discount percent (as a decimal): "))
AmountOff = MSRP * DiscountPercent
DiscountedPrice = MSRP - AmountOff
print(f"Make: {Make}")
print(f"Model: {Model}")
print(f"MSRP: ${MSRP:.2f}")
print(f"Discount Percent: {DiscountPercent * 100:.2f}%")
print(f"Amount Off: ${AmountOff:.2f}")
print(f"Discounted Price: ${DiscountedPrice:.2f}")

#5  Allow the user to enter a radius of a circle. Compute and display the area to be pi times radius squared (use 3.14 for
#   pi and multiple radius time radius for radius squared). Also, compute and display the perimeter (2 times pi * radius).

radius = float(input("Enter the radius of the circle: "))
pi = 3.14
area = pi * (radius ** 2)
perimeter = 2 * pi * radius
print(f"Area of the circle: {area:.2f}")
print(f"Perimeter of the circle: {perimeter:.2f}")