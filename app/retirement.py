#William Thompson (wtt53)
#Software Testing and QA
#Assignment 1: Test Driven Development
#Retirement: Takes current age (int), annual salary (float),
#percent of annual salary saved (float), and savings goal (float)
#and outputs what age savings goal will be met

def retirement(age, salary, percent, goal):

	try: #cast each variable as its proper data type
		age = int(age)
	except:
		return (False)

	try:
		salary = float(salary)
	except:
		return (False)

	try:
		percent = float(percent)
	except:
		return (False)

	try:
		goal = float(goal)
	except:
		return (False)

	if age < 15 or age > 99: #check each value to make sure it is in the proper range
		return (False)

	if salary <= 0:
		return (False)

	if percent <= 0:
		return (False)

	if goal <= 0:
		return (False)

	rawAnnualSavings = salary * (percent / 100)
	annualSavings = rawAnnualSavings + (rawAnnualSavings * 0.35)
	currentSavings = 0.00

	for i in range (age, 100):
		currentSavings += annualSavings
		if currentSavings >= goal:
			return("You will meet your savings goal at age "+str(i))

	return("Sorry, your goal won't be met.")