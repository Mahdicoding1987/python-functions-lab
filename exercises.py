def calculate_area_triangle(base, height):
    return base * height / 2

print('Exercise 1:', calculate_area_triangle(10, 5))

############################################################

def simple_interest(principal, rate, time):
    return principal * rate * time / 100

print('Exercise 2:', simple_interest(1000, 5, 2))

############################################################

def apply_discount(price, discount):
    return price - price * discount / 100

print('Exercise 3:', apply_discount(100, 25))

############################################################

def convert_temperature(celsius, Fahrenheit):
    return celsius * 9 / 5 + 32
    Fahrenheit = celsius * 9 / 5 + 32

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))

############################################################

def sum_to(n):
    return n * (n + 1) / 2

print('Exercise 5:', sum_to(10))

############################################################

def largest(a, b, c):
    return max(a, b, c)

print('Exercise 6:', largest(1, 2, 3))

############################################################

def calculate_tip(total_bill, tip_percentage):
    return total_bill * tip_percentage / 100

print('Exercise 7:', calculate_tip(50, 20))

############################################################

def product(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

print('Exercise 8:', product(2, 5, 5))

############################################################

def basicCalculator(num1, num2, operator):
    if operator == 'add':
        return num1 + num2
    elif operator == 'subtract':
        return num1 - num2
    elif operator == 'multiply':
        return num1 * num2
    elif operator == 'divide':
        return num1 / num2
    else:
        return "Invalid operator"

print('Exercise 9 Result:', basicCalculator(10, 5, "subtract"))