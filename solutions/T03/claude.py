def convert_temperature(value: float, source_unit: str, target_unit: str) -> float:
    """Convert temperature between Celsius (C), Fahrenheit (F), and Kelvin (K).

    Args:
        value: The temperature value to convert.
        source_unit: Source unit — one of 'C', 'F', 'K'.
        target_unit: Target unit — one of 'C', 'F', 'K'.

    Returns:
        Converted temperature rounded to 2 decimal places.

    Time complexity: O(1).  Space complexity: O(1).
    """
    _conversions = {
        ('C', 'F'): lambda x: x * 9 / 5 + 32,
        ('C', 'K'): lambda x: x + 273.15,
        ('F', 'C'): lambda x: (x - 32) * 5 / 9,
        ('F', 'K'): lambda x: (x - 32) * 5 / 9 + 273.15,
        ('K', 'C'): lambda x: x - 273.15,
        ('K', 'F'): lambda x: (x - 273.15) * 9 / 5 + 32,
    }
    if source_unit == target_unit:
        return round(value, 2)
    key = (source_unit, target_unit)
    return round(_conversions[key](value), 2)
