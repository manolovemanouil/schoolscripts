import random
import math


def f(x,y):

    term1 = x**2
    term2 = abs(x)
    term2 = math.sqrt(term2)
    term2 = y - term2
    term2 = term2**2
    result = term1 + term2

    return result

def is_inside_curve(point):

    x = point[0]
    y = point[1]

    val = f(x,y)

    if val >= 3:
        #this means the point lies outside the curve
        return False
    else:
        #this means the point lies inside the curve
        return True


def gen_point():
    x_coord = random.random()*4
    x_coord = x_coord - 2

    y_coord = random.random()*4.5
    y_coord = y_coord - 2

    point = (x_coord,y_coord)
    return point



num_points = 1000000
pointlist = []


for i in range(num_points):
    pointlist.append(gen_point())

counter = 0
for point in pointlist:
    if is_inside_curve(point) == True:
        counter += 1


ratio = counter/num_points

total_area = 4 * 4.5

area_of_heart = ratio*total_area

print("Area of heart: ", area_of_heart)


radius = math.sqrt(math.sqrt(3))
area_of_circle = (radius**2)*math.pi

resulting_area = area_of_heart - area_of_circle

print("Resulting area: ",resulting_area)