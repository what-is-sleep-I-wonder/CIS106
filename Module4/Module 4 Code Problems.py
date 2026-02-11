#1.	Allow the user to enter two exam scores from the keyboard. The first exam is worth 60% of the total
# points and the second exam is worth 40%. Calculate the total score by multiplying each exam score input
# by the respective weighting then add the two results together. Display the total. 

Exam1 = int(input("Enter the first exam score: "))
Exam2 = int(input("Enter the second exam score: "))
Exam1Weight = Exam1 * .60
Exam2Weight = Exam2 * .40
FinalScore = Exam1Weight + Exam2Weight
print("Your Final Score is", FinalScore)

#2.	Input the purchase price per share, the current stock price and quantity of stock, compute the
# increase (or decrease) of the value of the stock entered. (Value is computed as
# (current price – price per share) * quantity. If the amount is negative that means you are losing money).

PurchasePrice = float(input("Enter the purchase price per share:"))
CurrentPrice = float(input("Enter the current stock price:"))
Quantity = int(input("Enter the quantity of stock owned:"))
ValueChange = (CurrentPrice - PurchasePrice) * Quantity
print("The change in value of the stock is", ValueChange)
#DO NOT USE IF/THEN STATEMENT TO CHECK IF THE VALUE IS NEGATIVE. JUST DISPLAY THE VALUE CHANGE.


#3. Enter the total for a meal. Compute a tip at 15%, 18% and 20%. Display total, each tip value and total with each tip value. Your output
#should have total for the meal as entered, tip and total with tip for each tip value. (9 lines). Put a blank line between each tip of
#the set of tip values.

MealCoast = float(input("Enter the total for the meal: "))
Tip15 = 0.15
Tip18 = 0.18
Tip20 = 0.20
TipValue15 = MealCoast * Tip15
TipValue18 = MealCoast * Tip18
TipValue20 = MealCoast * Tip20
TotalWithTip15 = MealCoast + TipValue15
TotalWithTip18 = MealCoast + TipValue18
TotalWithTip20 = MealCoast + TipValue20
print("Total for the meal:", MealCoast)
print("Tip at 15%:", TipValue15)
print("Total with 15% tip:", TotalWithTip15)
print()
print("Total for the meal:", MealCoast)
print("Tip at 18%:", TipValue18)
print("Total with 18% tip:", TotalWithTip18)
print()
print("Total for the meal:", MealCoast)
print("Tip at 20%:", TipValue20)
print("Total with 20% tip:", TotalWithTip20)

#4. Enter first name and number of steps walked
#in a day. For each step you burned 0.25 calories. Computer the number of calories burned.
#Display first name and calories burned.

CalPerStep = 0.25
FirstName = input("Enter you first name: ")
StepsWalked = int(input("Enter the number of steps walked in a day: "))
CaloriesBurned = StepsWalked * CalPerStep
print(FirstName, "you burned", CaloriesBurned, "calories today.")

#5. You are setting up a business and need to compute the break-even point. This indicates how many items you must sell at a given
#price to cover your overhead. Enter fixed costs, price per unit and cost per unit into your program. Compute the break-even point
#by dividing fixed costs by the difference of price per unit and cost per unit.

FixedCosts = float(input("Enter your fixed costs: "))
PricePerUnit = float(input("Enter the price per unit: "))
CostPerUnit = float(input("Enter the cost per unit: "))
BreakEvenPoint = FixedCosts / (PricePerUnit - CostPerUnit)

print("The break-even point is", BreakEvenPoint, "units.")
