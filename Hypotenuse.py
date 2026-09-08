import math

#Ask the user to enter the length of two sides
sideA=float(input("enter the length of side A: "))
sideB=float(input("enter the length of side B: "))

#Compute the hypotenuse
c= math.sqrt (pow(sideA, 2) + (pow(sideB, 2)))

# Display the result rounded to two decimal places
print(f"The hypotenuse is: {c:.2f}")

