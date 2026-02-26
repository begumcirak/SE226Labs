import math

print("Enter a value for x1 : ")
x1 = float(input());
print("Enter a value for y1 : ")
y1 = float(input());
print("Enter a value for x2 : ")
x2 = float(input());
print("Enter a value for y2 : ")
y2 = float(input());

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("The distance between the two points is " +str(distance))
