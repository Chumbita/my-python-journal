import math

print("LET'S CALCULATE THE AREA OF A CIRCLE")

circle_radius = circle_area = int()
text_output = "The area of the circle is {} units^2"

circle_radius = int(input("-Enter the value of the circle's radius: "))
circle_area = math.pi * (circle_radius ** 2)

print(text_output.format(circle_area))


