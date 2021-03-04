import math

def f(x):



    term1 = 1/x
    term2 = math.cos(x)
    term3 = math.sin(x)/x #sinc(x) / sin(x)/x

    term4 = term2 - term3

    return term1*term4


def bisection_root(left, right):
    margin = 0.00001

    iterations = 0
    while True:

        lf = f(left)
        rf = f(right)
        c = right - left

        if c <= margin:
            break

        mid = (left + right) / 2

        if lf * f(mid) >= 0:
            left = mid
        else:
            right = mid

        iterations = iterations + 1

    print(iterations)

    return (left + right)/2



#first root between 4 and 5


root1 = bisection_root(4,5)

print(root1)


#second root between 7 and 8


root2 = bisection_root(7,8)

print(root2)



#third root between 10 and 12

root3 = bisection_root(10,12)

print(root3)



#fourth root between 13 and 15

root4 = bisection_root(13,15)

print(root4)


#fifth root between 16 and 18

root5 = bisection_root(16,18)

print(root5)







