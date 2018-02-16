def split_tip(tip, guest_count):
    try:
        float(tip)
    except Exception as e:
        return False
    try :
        int(guest_count)
    except Exception as e:
        return False

    if ((float(tip) == 0) \
    or (int(guest_count) == 0))\
    or (float(tip) == round(float(tip)))\
    or ((float(guest_count)) != round(float(guest_count))):
        return False

    if float(tip) == round(float(tip)):
        return False
    else:
        guest_count = int(guest_count)
        tip = float(tip)
        tip_split_var = tip / guest_count
        guest_array = [round(tip_split_var, 2)]
        total = tip - guest_array[0]
        for value in range(2, guest_count):
            guest_array.append(round(tip_split_var, 2))
            total = total - guest_array[value - 1]
        guest_array.append(round(total, 2))

        return guest_array
