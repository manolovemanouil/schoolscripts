import math
import matplotlib.pyplot as plt


def w(x):

    a = 7777
    v_0 = 14

    term1 = x/a
    term2 = x**2
    term2 = term2/(a**2)
    term3 = 4*v_0

    retval = (term1 - term2)*term3

    return retval


def dy_dx(x,y, v_b):
    term1 = y/x
    numerator = w(x)
    denominator = x**2 + y**2
    denominator = math.sqrt(denominator)
    denominator = x/denominator

    denominator = v_b * denominator

    term2 = numerator/denominator

    retval = term1 - term2

    return retval


def euler(delta_x, v_b):
    points = []
    initialpoint = (7777,0)
    points.append(initialpoint)
    x = 7777
    y = 0

    while True:

        if x <= 0:
            break

        slope = dy_dx(x,y,v_b)

        next_value = delta_x*slope

        y = y - next_value
        x = x - delta_x


        points.append((x,y))

    points.reverse()
    return points


v_7_points = euler(1,21)

xval = [v_7_points[x][0] for x in range(len(v_7_points))]
yval = [v_7_points[x][1] for x in range(len(v_7_points))]



plt.plot(xval,yval)
plt.ylim(0,11000)
plt.xlim(0,7777)
plt.show()




