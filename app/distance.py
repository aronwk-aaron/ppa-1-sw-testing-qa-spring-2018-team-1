def calc_distance(x1, y1, x2, y2):
	# checking for non int or float inputs
	if not(isinstance(x1, (float, int))):
		return False
	if not(isinstance(x2, (float, int))):
		return False
	if not(isinstance(y1, (float, int))):
		return False
	if not(isinstance(y2, (float, int))):
		return False

	# if the points are the same
	if ((x1 == x2) and (y1 == y2)):
		return 0
	# Calc distance
	else:
		distance = ((((x2-x1)**2)+((y2-y1)**2))**0.5)
		return round(distance,4)