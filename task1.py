#Nathan Wagstaff Assn 6 CS1400
#Polygon Area Calculator


#implementation
import math
from math import pi
from math import tan

#User input
numberOfSides = eval(input("How many sides does your polygon have?: "))
lengthOfSides = eval(input("How long is each side?: "))

#calculate answer
answer = (numberOfSides * math.pow(lengthOfSides, 2))/ (4 * tan(pi/ numberOfSides))

#round to 5 decimals
answer = round(answer, 5)

#print result
print(f"The area of your polygon with {numberOfSides} sides that have a length of {lengthOfSides} is {answer}")