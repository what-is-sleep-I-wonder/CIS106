#1 Create a dictionary with student name as the key and the grade as the value. Print student names and grades and class average grade in two columns with a header for each column.
students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

print(f"{'Student Name':<15} {'Grade':<10}")
print("-" * 25)

total_grade = 0
for name, grade in students.items():
    print(f"{name:<15} {grade:<10}")
    total_grade += grade

class_average = total_grade / len(students)
print("-" * 25)
print(f"{'Class Average':<15} {class_average:<10.2f}")

#2 Expand the dictionary above to have a list of three grades as the value. Create a function to create a list of three grade averages for the class. This list may be a dictionary, a list of lists
# ([name, average] as each element of the list, or some other list structure of your choice.  Print the list of students and their grade averages. Also print the class average for each of the three
# grades. Layout the output for ease of readability by the user.
students = {
    "Alice": [85, 90, 78],
    "Bob": [90, 92, 88],
    "Charlie": [78, 80, 82]
}
def calculate_averages(students):
    averages = []
    for name, grades in students.items():
        average = sum(grades) / len(grades)
        averages.append((name, average))
    return averages
averages = calculate_averages(students)
print(f"{'Student Name':<15} {'Average Grade':<15}")
print("-" * 30)
for name, average in averages:
    print(f"{name:<15} {average:<15.2f}")
grade_totals = [0, 0, 0]
for grades in students.values():
    for i in range(len(grades)):
        grade_totals[i] += grades[i]
grade_averages = [total / len(students) for total in grade_totals]
print("-" * 30)
print(f"{'Class Average':<15} {'':<15}")
for i, average in enumerate(grade_averages):
    print(f"Grade {i + 1}: {average:<15.2f}")

#3 Load list of 10 Player Names and Batting Averages from a file into a dictionary. (Create your own file with two items: player last name and batting average, i.e. 0.267, 0.300
#  etc, or use the file you created in the earlier problem set). Write a function to print the dictionary contents in two columns with a header for the name and average.
def load_players(filename):
    players = {}
    with open(filename, 'r') as file:
        for line in file:
            name, average = line.strip().split(',')
            players[name] = float(average)
    return players
def print_players(players):
    print(f"{'Player Name':<15} {'Batting Average':<15}")
    print("-" * 30)
    for name, average in players.items():
        print(f"{name:<15} {average:<15.3f}")
filename = 'players.txt'  # Make sure to create this file with player names and averages
players = load_players(filename)
print_players(players)