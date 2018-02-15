def calc_distance(x1, y1, x2, y2):
	# checking for non int or float inputs
	try:
		x1 = float(x1)
	except:
		raise ValueError("x1 must be a integer or a float")
	try:
		x2 = float(x2)
	except:		
		raise ValueError("x2 must be a integer or a float")
	try:
		y1 = float(y1)
	except:
		raise ValueError("y1 must be a integer or a float")
	try:
		y2 = float(y2)
	except:
		raise ValueError("y2 must be a integer or a float")

	# if the points are the same
	if ((x1 == x2) and (y1 == y2)):
		return 0
	# Calc distance
	else:
		distance = ((((x2-x1)**2)+((y2-y1)**2))**0.5)
		return round(distance,4)