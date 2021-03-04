import math
import time
from random import random
from random import seed


def f(x):

    denom = 1 + 25*(x**2)

    return 1/denom


def tangent_left(x):
    return 2.5*x + 1

def tangent_right(x):
    return -2.5*x + 1



def analyze_neg_x(x, y):

    if y > f(x):
        return 0 #not in area
    if y > tangent_left(x):
        #point is between curve and triangle
        return 1
    else:
        return 0

def analyze_non_neg(x,y):

    if y > f(x):
        return 0
    if y > tangent_right(x):
        return 1
    else:
        return 0


millis = int(round(time.time()*1000))
seed(millis)


# our range is  x = [-1, 1] and y = [1/26, 1] (starting at red line)


#y must be generated from  0 to 25/26, and then add +1/26 to it to keep points in range
#x must be generated from 0 to 2, then subtract 1

numpoints = 1000000

pointlist = []

for i in range(numpoints):

    xval = (random()*2) - 1
    yval = (random()*(25/26)) + (1/26)

    point = (xval, yval)

    pointlist.append(point)


in_area_counter = 0


for point in pointlist:

    xval = point[0]
    yval = point[1]

    if xval < 0:

        in_area_counter = in_area_counter + analyze_neg_x(xval,yval)

    else:
        in_area_counter = in_area_counter + analyze_non_neg(xval, yval)


#area is x times y or 2 * (25/26)
totalarea = 2 * (25/26)

proportion = in_area_counter / numpoints
area = proportion * totalarea

print("Points inside curve: ", in_area_counter)
print("Area: ", area)


def trapezoid_method(num):
    delta_x = 2/num

    area = 0

    curr_x = -1

    for i in range(num-1):

        b1 = f(curr_x)
        b2 = f(curr_x + delta_x)

        traparea = (b1 + b2)/2
        traparea = traparea * delta_x

        area += traparea

        curr_x += delta_x

    return area

#area of triangle is ~0.3698
#area under the red line is 2/26 or ~0.0769

iterations = 10000000
trap_area_estimate = trapezoid_method(iterations)
trap_area_estimate = trap_area_estimate - (0.3689 + 0.0769)

print("Trapezoid estimate with ", iterations, " trapezoids: ", trap_area_estimate)