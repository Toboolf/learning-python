import math

def calculate_circle_area(radius):
    return math.pi * radius**2

radius = float( input() )
area = calculate_circle_area(radius)

print(area)
