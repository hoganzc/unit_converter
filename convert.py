def get_unit(unit):
    return_units = {
        "lbs": "kg",
        "oz": "kg",
        "ft": "mm",
        "in": "mm",
        "pint": "liters",
        "gal": "liters",
        "mi": "km"
    }

    return return_units[unit]


def convert(unit, amount):
    LBS_TO_KG = 0.453592
    OZ_TO_KG = 0.0283495
    FEET_TO_MM = 304.8
    IN_TO_MM = 25.4
    PINT_TO_LITER = 0.473176
    GALLON_TO_LITER = 3.78541
    MI_TO_KM = 1.60934

    if unit == 'lbs':
        return amount * LBS_TO_KG
    elif unit == 'oz':
        return amount * OZ_TO_KG
    elif unit == 'ft':
        return amount * FEET_TO_MM
    elif unit == 'in':
        return amount * IN_TO_MM
    elif unit == 'pint':
        return amount * PINT_TO_LITER
    elif unit == 'gal':
        return amount * GALLON_TO_LITER
    elif unit == 'mi':
        return amount * MI_TO_KM
