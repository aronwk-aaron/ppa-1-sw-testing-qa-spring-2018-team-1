import os # pragma: no cover
import sys # pragma: no cover
os.system('cls') # pragma: no cover
from tip import split_tip # pragma: no cover

def main(): # pragma: no cover
    print("Welcome to Team 1's Profesional Practice Project!\n"
          "1. Body Mass Index\n"
          "2. Retirement\n"
          "3. Shortest Distance\n"
          "4. Email Verifier\n"
          "5. Split the Tip\n"
          "6. Exit the Application")
    while True:
        choice = input("Please enter the number of what you would like to do: ")

        if (choice == "1"):
            BMI_input()
        elif (choice == "2"):
            retirement_input()
        elif (choice == "3"):
            distance_input()
        elif (choice == "4"):
            email_input()
        elif (choice == "5"):
            tip_input()
        elif (choice == "6"):
            sys.exit("Exiting Program")
        else:
            print("Invalid input.")


def BMI_input(): # pragma: no cover
    print()
    feet = input("Enter your height (feet): ")
    inches = input("Height (inches): ")
    weight = input("Enter your weight in pounds: ")

    bmi_status, bmi = calc_bmi(feet, inches, weight)
    print(bmi_status,": ", bmi)
    print()

def retirement_input(): # pragma: no cover
    age = input("Enter your age: ")
    salary = input("Enter your annual salary: ")
    precent = input("Enter your percent saved (10% would be 10): ")
    goal = input("Enter your retirement saving goal: ")

    print(retirement(age, salary, precent, goal))

    # output

def distance_input(): # pragma: no cover
    print()
    x1 = input("Input your first x point: ")
    y1 = input("Input your first y point: ")
    x2 = input("Input your second x point: ")
    y2 = input("Input your second y point: ")

    dist = calc_distance(x1, y1, x2, y2)
    print("The shortest distance between the two points is ", dist)
    print()

def email_input(): # pragma: no cover
    print()
    email = input("Enter your email address: ")
    if verify_email(email):
        print(email, " is an email")
    else:
        print(email, " is not an email")
    print()

def tip_input(): # pragma: no cover
    bill = input("Enter the ammount for the check: ")
    people = input("Enter the number of people in your party: ")
    payment_list = split_tip(bill, people)
    print()

    if payment_list == False:
        print("invalid input")
        print()
        return

    i = 1
    for each in payment_list:
        print("guest ", i, " pays ", each, "\n")
    print()


main() # pragma: no cover
