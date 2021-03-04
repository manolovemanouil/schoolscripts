import random
import math


class Line:
    def __init__(self, end1, end2, length):
        self.end1 = end1
        self.end2 = end2
        self.length = length

    def check_bounds(self):



        if self.length < 0.005:
            return False
        e1_in = in_bounds(self.end1[0], self.end1[1])
        e2_in = in_bounds(self.end2[0], self.end2[1])

        if e1_in != e2_in:
            return True

        else:
            if Line(self.end1,midpoint(self),self.length/2).check_bounds() == True:
                return True
            elif Line(midpoint(self),self.end2, self.length/2).check_bounds() == True:
                return True
            else:
                return False

    def lprint(self):
        print(self.end1)
        print(self.end2)
        print(self.length)

    def extremety_check(self):
        #checks if line lies  entirely outside the possibility of intersection
        if self.end1[0] < -0.78 and self.end2[0] < -0.78:
            return True
        if self.end1[0] > 0.78 and self.end2[0] > 0.78:
            return True
        if self.end1[1] > 0.78 and self.end2[1] > 0.78:
            return True
        if self.end1[1] < -0.78 and self.end2[1] < -0.78:
            return True
        else:
            return False


def midpoint(line):

    x1 = line.end1[0]
    x2 = line.end2[0]
    y1 = line.end1[1]
    y2 = line.end2[1]

    return ((x1+x2)/2 , (y1+y2)/2)

def gen_line(length):

    #our bounds are x = (-1,1) and y = (-1,1)

    center_x = random.random()*2
    center_x = center_x - 1

    center_y = random.random()*2
    center_y = center_y - 1

    angle = random.random()*360
    angle = math.radians(angle)

    xoffset = (length*math.cos(angle))/2
    yoffset = (length*math.sin(angle))/2

    end1_x = center_x + xoffset
    end1_y = center_y + yoffset

    end2_x = center_x - xoffset
    end2_y = center_y - yoffset

    end1 = (end1_x, end1_y)
    end2 = (end2_x, end2_y)

    return Line(end1,end2,length)


def in_bounds(x,y):

    theta = math.atan((y/x))

    r_curve = math.sin(2*theta)

    r_point = math.sqrt(x**2 + y**2)

    if r_curve >= r_point:
        return True
    else:
        return False


l_len = 0.1
num_lines = 1000000
line_list = []

for i in range(num_lines):

    line_list.append(gen_line(l_len))



lines_touching = 0

for line in line_list:
    #line.lprint()

    if line.extremety_check() == True:
        continue
        #this means the line lies outside the possible bounds of the function

    if line.check_bounds() == True:
        lines_touching += 1


print(lines_touching)



