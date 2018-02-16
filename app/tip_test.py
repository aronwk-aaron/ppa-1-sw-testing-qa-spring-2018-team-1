import pytest


def split_tip(tip, guest):
    if not (isinstance(tip, (float))):
        raise ValueError("Your tip must be a float value")
    if not (isinstance(guest, (int))):
        raise ValueError("Your guest must be an integer")

    if (tip == 0):
        print("Tip value cannot be 0")
        return 0

    elif (guest == 0):
        print("Cannot have 0 guest")
        return 0

    else:
        tip_split_var = tip / guest
        guest_array = [round(tip_split_var, 2)]
        total = tip - guest_array[0]
        for value in range(2, guest):
            guest_array.append(round(tip_split_var, 2))
            total = total - guest_array[value - 1]
        guest_array.append(round(total, 2))
        return guest_array
