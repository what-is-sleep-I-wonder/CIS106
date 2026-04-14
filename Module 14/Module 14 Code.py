#1 Create a class.  Add a method to the class that accepts a bonus rate for the employee. It should then compute the employee bonus of rate x
# salary and return this value. Demonstrate this method works by entering a bonus rate and displaying the bonus
class Employee:
    first_name = ""
    last_name = ""
    address = ""
    city = ""
    state = ""
    zip_code = ""
    employee_id = ""
    salary = 0.00
    # Method to compute employee bonus
    def compute_bonus(self, bonus_rate):
        bonus = self.salary * bonus_rate
        return bonus
# Create instance of Employee class and set attributes
employee1 = Employee()
employee1.first_name = "Jane"
employee1.last_name = "Doe"
employee1.address = "123 Main St"
employee1.city = "Anytown"
employee1.state = "IL"
employee1.zip_code = "12345"
employee1.employee_id = "E001"
employee1.salary = 60000.00
bonus_rate = 0.10
print(employee1.compute_bonus(bonus_rate))

#2 Create a student class. This class should consist of student first name, student last name, district code (I or O) and enrolled credits.
# Create a method to compute tuition owed. Tuition owed should be enrolled credits times $250.00 per credit hour for in district students
# (district code of I) and or times $500.00 per credit hour for out of district students (district code of anything other than I). Test the
# class by instantiating the object and adding data.
class Student:
    first_name = ""
    last_name = ""
    district_code = ""
    enrolled_credits = 0
    # Method to compute tuition owed
    def compute_tuition(self):
        if self.district_code == "I":
            tuition = self.enrolled_credits * 250.00
        else:
            tuition = self.enrolled_credits * 500.00
        return tuition
# Create instance of Student class
student1 = Student()
student1.first_name = "John"
student1.last_name = "Smith"
student1.district_code = "I"
student1.enrolled_credits = 15
print(f"Tuition owed for {student1.first_name} {student1.last_name}: ${student1.compute_tuition():.2f}")

#3 Modify problem 2 to use a dictionary for the district code pair. Make sure it works. Expand the dictionary to include X for
# international students whose tuition is $800.00 per credit hour and G for reciprocity students whose tuition the same as an I student.
# Instantiate at least one student of each district code.
class Student:
    first_name = ""
    last_name = ""
    # Use a dictionary to store district codes and their corresponding tuition rates
    tuition_rates = {"I": 250.00, "G": 250.00, "X": 800.00}
    district_code = ""
    enrolled_credits = 0
    # Method to compute tuition owed
    def compute_tuition(self):
        tuition_rate = self.tuition_rates.get(self.district_code, 500.00)  # Default to 500.00 for out of district
        tuition = self.enrolled_credits * tuition_rate
        return tuition
# Create instance of Student class
student1 = Student()
student1.first_name = "John"
student1.last_name = "Smith"
student1.district_code = "I"
student1.enrolled_credits = 15
print(f"Tuition owed for {student1.first_name} {student1.last_name}: ${student1.compute_tuition():.2f}")
student2 = Student()
student2.first_name = "Emily"
student2.last_name = "Johnson"
student2.district_code = "X"
student2.enrolled_credits = 15
print(f"Tuition owed for {student2.first_name} {student2.last_name}: ${student2.compute_tuition():.2f}")
student3 = Student()
student3.first_name = "Michael"
student3.last_name = "Brown"
student3.district_code = "G"
student3.enrolled_credits = 15
print(f"Tuition owed for {student3.first_name} {student3.last_name}: ${student3.compute_tuition():.2f}")