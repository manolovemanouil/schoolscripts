
def f(x,y):

    return x + y + x*y

x = 0
y = 1   #initial y value
delta_x = 0.01

initial_point = (0,1)

points = []
points.append(initial_point)

while True:

    if x >= 0.50:
        break

    slope = f(x, y)

    next_value = delta_x*slope


    y = y + next_value
    x = x + delta_x
    x = round(x, 2)

    points.append((x,y))



print(points)


#the following were just to get copy/pastable printouts for my report and for excel spreadsheets

for point in points:

    print("y(",point[0],") = ",point[1])


for point in points:
    print(point[0])

for point in points:
    print(point[1])