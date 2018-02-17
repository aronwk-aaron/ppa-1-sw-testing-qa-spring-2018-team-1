#William Thompson (wtt53)
#Software Testing and QA
#Assignment 1: Test Driven Development
#Retirement: Takes current age (int), annual salary (float),
#percent of annual salary saved (float), and savings goal (float)
#and outputs what age savings goal will be met

def retirement(age, salary, percent, goal):

	age = int(age) #cast each variable as its proper data type
	salary = float(salary)
	percent = float(percent)
	goal = float(goal)

	if age < 15 or age > 99: #check each value to make sure it is in the proper range
		raise(ValueError("Age must be between 15 and 99"))

	if salary <= 0:
		raise(ValueError("Salary must be greater than 0"))

	if percent <= 0:
		raise(ValueError("Percent saved must be greater than 0"))

	if goal <= 0:
		raise(ValueError("Goal must be greater than 0"))

	rawAnnualSavings = salary * (percent / 100)
	annualSavings = rawAnnualSavings + (rawAnnualSavings * 0.35)
	currentSavings = 0.00

	for i in range (age, 100):
		currentSavings += annualSavings
		if currentSavings >= goal:
			return("You will meet your savings goal at age "+str(i))

	return("Sorry, your goal won't be met.")