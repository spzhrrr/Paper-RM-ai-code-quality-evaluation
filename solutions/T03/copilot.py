def convert_temperature(value, source_unit, target_unit):
    if source_unit == 'C':
        if target_unit == 'F':
            return round(value * 9/5 + 32, 2)
        elif target_unit == 'K':
            return round(value + 273.15, 2)
        else:
            return round(value, 2)
    elif source_unit == 'F':
        if target_unit == 'C':
            return round((value - 32) * 5/9, 2)
        elif target_unit == 'K':
            return round((value - 32) * 5/9 + 273.15, 2)
        else:
            return round(value, 2)
    elif source_unit == 'K':
        if target_unit == 'C':
            return round(value - 273.15, 2)
        elif target_unit == 'F':
            return round((value - 273.15) * 9/5 + 32, 2)
        else:
            return round(value, 2)
    return round(value, 2)
