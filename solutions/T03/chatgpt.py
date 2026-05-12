def convert_temperature(value, source_unit, target_unit):
    if source_unit == target_unit:
        return round(value, 2)
    if source_unit == 'F':
        celsius = (value - 32) * 5 / 9
    elif source_unit == 'K':
        celsius = value - 273.15
    else:
        celsius = value
    if target_unit == 'F':
        return round((celsius * 9 / 5) + 32, 2)
    elif target_unit == 'K':
        return round(celsius + 273.15, 2)
    else:
        return round(celsius, 2)
