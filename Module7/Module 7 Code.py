# Display the odd numbers starting at 1 and ending with 25. Use a while loop structure for this problem.
number = 1
while number <= 25:
    print(number)
    number += 2

# Allow the user to enter a start value, stop value and increment value from the keyboard. Display all the
# numbers from the start value to stop value using the increment value as you proceed. Use a while loop structure for this problem.
start_value = int(input("Enter the start value: "))
stop_value = int(input("Enter the stop value: "))
increment_value = int(input("Enter the increment value: "))
while start_value <= stop_value:
    print(start_value)
    start_value += increment_value

# Prompt the user on whether they want to do this program (just before the while loop). “Yes” entry means they want to continue.
# Any other response indicates they will stop the program. This response is the loop control variable. If the user answers “Yes “then go into the while loop.
# Once in the while loop. You are to prompt the user for their last name and two exam scores. Compute the average exam score. Display last name and average.
# After the loop, display a count of the number of students who entered data.
count = 0
response = input("Do you want to enter student data? (Yes/No): ")
while response.lower() == "yes":
    last_name = input("Enter the student's last name: ")
    exam_score1 = float(input("Enter the first exam score: "))
    exam_score2 = float(input("Enter the second exam score: "))
    average_score = (exam_score1 + exam_score2) / 2
    print(f"{last_name}'s average exam score is: {average_score:.2f}")
    count += 1
    response = input("Do you want to enter student data? (Yes/No): ")
print(f"Total number of students who entered data: {count}")

# Prompt the user on whether they want to do this program (just before the while loop). Yes means they want to continue. Any other response indicates they will stop the program.
# This response is the loop control variable. If the user answers Yes then go into the while loop. Once in the while loop. You are to prompt the user for employee last name, hours worked and rate of pay.
# Compute gross pay. Give the employee time and a half for hours worked over 40. Sum the gross pay and count the number of employees.
# After the loop (all data entered) display the sum of all the gross pays, and count of the number of employees. Compute and display the average pay.

count = 0
total_gross_pay = 0.0
response = input("Do you want to enter employee data? (Yes/No): ")
while response.lower() == "yes":
    last_name = input("Enter the employee's last name: ")
    hours_worked = float(input("Enter hours worked: "))
    rate_of_pay = float(input("Enter rate of pay: "))
    
    if hours_worked > 40:
        gross_pay = (40 * rate_of_pay) + ((hours_worked - 40) * rate_of_pay * 1.5)
    else:
        gross_pay = hours_worked * rate_of_pay
    
    print(f"{last_name}'s gross pay is: {gross_pay:.2f}")
    
    total_gross_pay += gross_pay
    count += 1
    
    response = input("Do you want to enter employee data? (Yes/No): ")
if count > 0:
    average_pay = total_gross_pay / count
    print(f"Total gross pay for all employees: {total_gross_pay:.2f}")
    print(f"Total number of employees: {count}")
    print(f"Average pay: {average_pay:.2f}")

# Prompt the user on whether they want to do this program (just before the while loop). Yes means they want to continue. Any other response indicates they will stop the program.
# This response is the loop control variable. If the user answers Yes then go into the while loop. Once in the while loop. You are to prompt the user for quantity and price of an item.
# Compute extended price (quantity times price of an item. If the extended price is greater than 10000.00 compute a discount of 25%. All other orders get a 10% discount.
# For each order display extended price, discount amount (extended price x discount percent), total (extended price – discount amount). For each order sum the discount amount.
# After the loop (all data entered) display the sum of all the discounts. Finally, the last statements within the while loop will ask the user if they want to do this loop again.
# In other words, the user needs to be prompted again. The reason is that the end of the loop takes execution to the while condition to be evaluated again.
# It cannot take us to the first few lines of code that prompt the user for the first time. That code is out of the loop. Therefore, we need a second prompt at the bottom, inside the loop.
total_discount = 0.0
response = input("Do you want to enter order data? (Yes/No): ")
while response.lower() == "yes":
    quantity = int(input("Enter the quantity of the item: "))
    price = float(input("Enter the price of the item: "))
    
    extended_price = quantity * price
    
    if extended_price > 10000.00:
        discount_percent = 0.25
    else:
        discount_percent = 0.10
    
    discount_amount = extended_price * discount_percent
    total = extended_price - discount_amount
    
    print(f"Extended price: {extended_price:.2f}")
    print(f"Discount amount: {discount_amount:.2f}")
    print(f"Total after discount: {total:.2f}")
    
    total_discount += discount_amount
    
    response = input("Do you want to enter order data? (Yes/No): ")
print(f"Total discount amount for all orders: {total_discount:.2f}")