def calculate_fuel(mass):
    # if type(mass) != int:
    #     return False

    try:
        mass = int(mass)
    except (TypeError, ValueError):
        return False

    if mass < 0:
        return False
    elif 0 < mass < 9:
        return 1

    fuel = mass // 3 - 2
    return fuel
