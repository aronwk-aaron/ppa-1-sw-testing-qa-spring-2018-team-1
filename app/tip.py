def split_tip(tip, guest_count):
    if not (isinstance(tip, (float))):
        return False
    if not (isinstance(guest_count, (int))):
        return False

    if ((tip == 0) or (guest_count == 0)):
        return False

    else:
        tip_split_var = tip / guest_count
        guest_array = [round(tip_split_var, 2)]
        total = tip - guest_array[0]
        for value in range(2, guest_count):
            guest_array.append(round(tip_split_var, 2))
            total = total - guest_array[value - 1]
        guest_array.append(round(total, 2))

        return guest_array
