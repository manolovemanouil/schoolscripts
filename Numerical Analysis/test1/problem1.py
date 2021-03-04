import math
import time
from random import random
from random import seed

def get_x(tval):

    term1 = tval**5
    term2 = 4 * (tval**3)

    return term1 - term2


millis = int(round(time.time() * 1000))

seed(millis) #seeding the random algorithm with the current time in milliseconds

#setting up the area bounds

xmin = -6
xmax = 6
ymin = 0
ymax = 4

pointlist = []

#generating random points in this range

#for x-values generate value from 0 to 12, then subtract 6
#for y values generate value from 0 to 4

for i in range(0, 50000):
#generate 50 thousand points
    xval = (random()*12)-6
    yval = random()*4
    point = (xval,yval)

    pointlist.append(point)


in_area_counter = 0

for point in pointlist:

    xval = point[0]
    yval = point[1]

    tval = math.sqrt(yval)

    if xval < 0:
        tval = tval * -1

        x_of_curve = get_x(tval)
        x_of_curve = x_of_curve * -1

        if xval > x_of_curve:
            in_area_counter = in_area_counter + 1


    else:
        #x is positive, and counts if it is to  left of curve
        x_of_curve = get_x(tval)

        if xval < x_of_curve:
            in_area_counter = in_area_counter + 1




#get the total area now

totalarea = 12 * 4 #-6 to 6 is 12 and 0 to 4 is 4

proportion = in_area_counter / 50000 #proportion of points inside the area

area_of_curve = proportion * totalarea

print("Points inside curve: ",in_area_counter)

print("Area: ", area_of_curve)


