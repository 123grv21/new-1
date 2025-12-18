import math
number = float(input("Enter a number:"))

if number <= 0:
    print("please enter a positive number fror logarithm and square root")
else:
    print("square root:",math.sqrt(number))
    print("natural logarithm:",math.log(number))
    print("sine value:",math.sin(number))