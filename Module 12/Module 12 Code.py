#1
#Assign 10 last names to a list.
# Write a function to display the names.
# Write Another function to display the names in reverse order.
LastName = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

def display_names(names):
    for name in names:
        print(name)

def display_names_reverse(names):
    for name in reversed(names):
        print(name)

print("Names in original order:")
display_names(LastName)
print("Names in reverse order:")
display_names_reverse(LastName)

#2
#Add another list to #1 for exam scores
#Write a function to display the names and scores together.
ExamScores = [85, 92, 78, 90, 88, 95, 80, 91, 89, 94]
def display_names_and_scores(names, scores):
    for name, score in zip(names, scores):
        print(f"{name}: {score}")
print("Names and Exam Scores:")
display_names_and_scores(LastName, ExamScores)
print( )

#3
# Write the code for the following problem. The data to load is lastname and score. You can do this from a file as done in an earlier exercise. 
# Add a function to the program to display the last name and highest score, last name and lowest score.
def displayResults(highName, highScore, lowName, lowScore):
    print("The Highest Score is " + str(highScore) + " belonging to " + highName)
    print("The Lowest Score is " + str(lowScore) + " belonging to " + lowName)

# Main
lastName = [""] * (10)
scoreList = [0] * (10)

counter = 0
firstRecord = True
infile = open("Problem 3 File.txt", 'r')
nextLine = infile.readline()
while not nextLine == '':
    name = nextLine
    nextLine = infile.readline()
    score = nextLine
    nextLine = infile.readline()
    lastName[counter] = name
    scoreList[counter] = int(score)
    counter = counter + 1
    if firstRecord:
        highScore = int(score)
        lowScore = int(score)
        highName = name
        lowName = name
        firstRecord = False
    else:
        if int(score) > highScore:
            highScore = int(score)
            highName = name
        if int(score) < lowScore:
            lowScore = int(score)
            lowName = name
infile.close()
displayResults(highName, highScore, lowName, lowScore)

#4
# Load list of 10 Player Names and Batting Averages from a file into arrays, one of names and the other of averages.
# Write a function to display the two arrays.Write another function to search for the last name in the array and then display last name and batting average when found.
# Then use a while loop in the main program to repeatedly ask the user for a last name
# until the user enters “exit” to end the program.
#5
# Display a message, “Name not found” when the name is not in the list. 
def displayPlayers(names, averages):
    for name, average in zip(names, averages):
        print(f"{name}: {average}")
def searchPlayer(names, averages, searchName):
    for name, average in zip(names, averages):
        if name.strip() == searchName.strip():
            return f"{name}: {average}"
    return "Name not found"
# Main
playerNames = [""] * (10)
playerAverages = [0.0] * (10)
infile = open("Problem 4 File.txt", 'r')
counter = 0
nextLine = infile.readline()
while not nextLine == '':
    name = nextLine
    nextLine = infile.readline()
    average = nextLine
    nextLine = infile.readline()
    playerNames[counter] = name
    playerAverages[counter] = float(average)
    counter = counter + 1
infile.close()
print("Player Names and Batting Averages:")
displayPlayers(playerNames, playerAverages)
while True:
    searchName = input("Enter a last name to search (or 'exit' to quit): ")
    if searchName.lower() == 'exit':
        break
    result = searchPlayer(playerNames, playerAverages, searchName)
    print(result)