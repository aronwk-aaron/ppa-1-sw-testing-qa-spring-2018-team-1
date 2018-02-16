import pytest


def split_tip(tip, guest):
    if not (isinstance(tip, (float, int))):
        raise ValueError("x1 must be a integer or a float")
    if not (isinstance(guest, (int))):
        raise ValueError("x2 must be a integer or a float")

    if ((tip == 0) or (guest == 0)):
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
