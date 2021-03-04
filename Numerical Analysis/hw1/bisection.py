import math

def f(x):
    term1 = 2.020**(-x**3)
    term2 = -(x**4)*(math.sin(x**3))
    term3 = -1.949

    return term1 + term2 + term3


def root(left, right):
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


#first root

#interval [-1, -0.5]

root1 = root(-1, -0.5)

print(root1)


#second root
#interval [1, 1.7]

root2 = root(1, 1.7)

print(root2)


#third root
#interval [1.6, 2]

root3 = root(1.6, 2)

print(root3)





