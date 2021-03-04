import numpy as np
x = [0.1,0.2,0.3,0.4,0.5]
y = [1.1141842615436537, 1.2637194336484336, 1.455997623426589, 1.7006938833473375, 2.0104749566723124]

y.reverse()
x.reverse()


left_matrix = [[0 for i in range(5)] for j in range(5)]

for i in range(5):
    for j in range(5):
        left_matrix[i][j] = round(x[i]**(4-j), 6)



l_inverse = np.linalg.inv(left_matrix)


a_vector = np.matmul(l_inverse,y)

print(a_vector)
