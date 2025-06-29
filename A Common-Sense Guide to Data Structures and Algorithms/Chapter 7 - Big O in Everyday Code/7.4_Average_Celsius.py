

'''
Forth Algorithm: Converts all reading from Fahrenheit to Celsius then finds the 
average of all the Celsius numbers for our weather-forecasting software.
'''

def average_celsius(fahrenheit_readings):
    # Collect Celsius numbers here:
    celsius_numbers = []
    # Convert each reading to Celsius and add to array:
    for fahrenheit_reading in fahrenheit_readings:
        celsius_conversion = (fahrenheit_reading - 32) / 1.8
        celsius_numbers.append(celsius_conversion)
    # Get sum of all Celsius numbers:
    sum = 0.0
    for celsius_number in celsius_numbers:
        sum += celsius_number
    # Return mean average:
    return sum / len(celsius_numbers)
