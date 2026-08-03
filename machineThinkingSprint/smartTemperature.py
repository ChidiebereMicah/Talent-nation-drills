"""
SmartTemperature
Instructions

Implement smart_temperature(value). 
Convert value to a Celsius number. 
If conversion fails, return Invalid temperature. 
Convert Celsius to Fahrenheit using the standard formula. 
Return a three-line report with labels Celsius, Fahrenheit, and Status. 
Status is freezing when Celsius is less than or equal to 0, 
cold when below 20, warm when from 20 through 30, and hot when above 30.
"""

def smart_temperature(value):
    try:
        celsius = round(float(value),2)
    except Exception:
        return "Invalid temperature"
    
    fahrenheit = (celsius * 9/5) + 32

    if celsius <= 0:
        status = "freezing"
    elif celsius < 20:
        status = "cold"
    elif celsius <= 30:
        status = "warm"
    else:
        status = "hot"

    return f"Celsius: {celsius}\nFahrenheit: {fahrenheit}\nStatus: {status}"