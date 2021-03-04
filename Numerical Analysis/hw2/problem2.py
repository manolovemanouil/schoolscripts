import random


#2^10 is 1024


first_matrix = [[random.uniform(-1,1) for i in range(1024)] for j in range(1024)]
second_matrix = [[random.uniform(-1,1) for i in range(1024)] for j in range(1024)]

#print(len(first_matrix[0]))

#this was just a test matrix

f = [[2 , 2 , 2 , 6 , 5 , 3 , 3 , 6],
[5 , 0 , 2 , 8 , 8 , 9 , 1 , 2],
[0 , 1 , 1 , 8 , 5 , 5 , 7 , 8],
[5 , 8 , 9 , 1 , 0 , 1 , 5 , 5],
[7 , 2 , 2 , 8 , 4 , 0 , 0 , 1],
[5 , 8 , 1 , 3 , 0 , 4 , 7 , 8],
[6 , 0 , 0 , 0 , 3 , 0 , 3 , 1],
[3 , 4 , 1 , 2 , 4 , 0 , 9 , 2]]
s = [[0 , 9 , 5 , 7 , 8 , 3 , 9 , 8],
[2 , 7 , 9 , 2 , 7 , 3 , 8 , 9],
[2 , 7 , 9 , 7 , 8 , 7 , 9 , 9],
[7 , 3 , 0 , 1 , 5 , 4 , 4 , 0],
[9 , 4 , 6 , 3 , 8 , 5 , 7 , 8],
[4 , 4 , 6 , 4 , 8 , 1 , 0 , 3],
[1 , 1 , 7 , 6 , 6 , 7 , 4 , 0],
[0 , 1 , 6 , 3 , 0 , 8 , 8 , 2]]


def naive_mult(mat1, mat2):

    matlen = len(mat1[0])

    result_matrix = [[0 for i in range(matlen)] for j in range(matlen)]

    for i in range(matlen):
        for j in range(matlen):
            val = 0
            for k in range(matlen):
                val = val + mat1[i][k] * mat2[k][j]


            result_matrix[i][j] = val


    return result_matrix

def add_mats(m1, m2):
    l = len(m1[0])
    nmat = [[0 for i in range(l)] for j in range(l)]
    for i in range(l):
        for j in range(l):
            nmat[i][j] = m1[i][j] + m2[i][j]

    return nmat

def sub_mats(m1,m2):
    l = len(m1[0])
    nmat = [[0 for i in range(l)] for j in range(l)]
    for i in range(l):
        for j in range(l):
            nmat[i][j] = m1[i][j] - m2[i][j]

    return nmat


def strassen(m1,m2):

    l = len(m1[0])

    res = [[0 for i in range(l)] for j in range(l)]

    if l == 2:
        p1 = m1[0][0]*(m2[0][1] - m2[1][1])
        p2 = (m1[0][0]+m1[0][1])*m2[1][1]
        p3 = (m1[1][0]+m1[1][1])*m2[0][0]
        p4 = m1[1][1]*(m2[1][0]-m2[0][0])
        p5 = (m1[0][0]+m1[1][1])*(m2[0][0]+m2[1][1])
        p6 = (m1[0][1]-m1[1][1])*(m2[1][0]+m2[1][1])
        p7 = (m1[0][0]-m1[1][0])*(m2[0][0]+m2[0][1])

        res[0][0] = p5 + p4 - p2 + p6
        res[0][1] = p1 + p2
        res[1][0] = p3 + p4
        res[1][1] = p1 + p5 - p3 - p7

    else:

        nlen = l//2

        a11 = [[0 for i in range(nlen)] for j in range(nlen)]
        a12 = [[0 for i in range(nlen)] for j in range(nlen)]
        a21 = [[0 for i in range(nlen)] for j in range(nlen)]
        a22 = [[0 for i in range(nlen)] for j in range(nlen)]

        b11 = [[0 for i in range(nlen)] for j in range(nlen)]
        b12 = [[0 for i in range(nlen)] for j in range(nlen)]
        b21 = [[0 for i in range(nlen)] for j in range(nlen)]
        b22 = [[0 for i in range(nlen)] for j in range(nlen)]

        for i in range(nlen):
            for j in range(nlen):
                a11[i][j] = m1[i][j]
                a12[i][j] = m1[i][j + nlen]
                a21[i][j] = m1[i + nlen][j]
                a22[i][j] = m1[i + nlen][j + nlen]

                b11[i][j] = m2[i][j]
                b12[i][j] = m2[i][j + nlen]
                b21[i][j] = m2[i + nlen][j]
                b22[i][j] = m2[i + nlen][j + nlen]


        p1 = strassen(a11, sub_mats(b12,b22))
        p2 = strassen(add_mats(a11,a12),b22)
        p3 = strassen(add_mats(a21,a22),b11)
        p4 = strassen(a22,sub_mats(b21,b11))
        p5 = strassen(add_mats(a11,a22),add_mats(b11,b22))
        p6 = strassen(sub_mats(a12,a22),add_mats(b21,b22))
        p7 = strassen(sub_mats(a11,a21),add_mats(b11,b12))


        c11 = add_mats(add_mats(p5,p6),sub_mats(p4,p2))
        c12 = add_mats(p1,p2)
        c21 = add_mats(p3,p4)
        c22 = add_mats(sub_mats(p5,p3),sub_mats(p1,p7))


        for i in range(nlen):
            for j in range(nlen):
                res[i][j] = c11[i][j]
                res[i][j+nlen] = c12[i][j]
                res[i+nlen][j] = c21[i][j]
                res[i+nlen][j+nlen] = c22[i][j]

    return res



#print(strassen(first_matrix,second_matrix))

first_matrix_bigger = [[random.uniform(-1,1) for i in range(4096)] for j in range(4096)]
second_matrix_bigger = [[random.uniform(-1,1) for i in range(4096)] for j in range(4096)]

print(strassen(first_matrix_bigger,second_matrix_bigger))






