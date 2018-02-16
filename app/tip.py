<<<<<<< Updated upstream
def split_tip(tip,guest_count):
        
		tip_split_var = tip / guest_count
		guest_array=[round(tip_split_var,2)]
		total = tip - guest_array[0]
		for value in range(2,guest_count):
			guest_array.append(round(tip_split_var,2))
			total = total - guest_array[value-1]
		guest_array.append(round(total,2))



		return guest_array

def main():
	
		total = split_tip(15.18, 3)

		for value in range(0,len(total)):
			print(total[value])

main()
=======
def split_tip(tip,guest_count):
        
		tip_split_var = tip / guest_count
		guest_array=[round(tip_split_var,2)]
		total = tip - guest_array[0]
		for value in range(2,guest_count):
			guest_array.append(round(tip_split_var,2))
			total = total - guest_array[value-1]
		guest_array.append(round(total,2))



		return guest_array

def main():
	
		total = split_tip(15.18, 3)

		for value in range(0,len(total)):
			print(total[value])

main()
>>>>>>> Stashed changes
