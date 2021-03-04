import numpy as np
import math


def gen_normal_number(mu, sigma):

    #as per steps defined in lecture

    x1 = np.random.normal(0,1)
    x2 = np.random.normal(0,1)

    cos_term = 2*math.pi*x2
    sin_term = 2*math.pi*x2

    cos_term = math.cos(cos_term)
    sin_term = math.sin(sin_term)

    ln_term = math.log(x1)
    ln_term = ln_term * (-2)
    ln_term = math.sqrt(ln_term)

    g1 = ln_term*cos_term
    g2 = ln_term*sin_term

    z1 = mu + g1*sigma
    z2 = mu + g1*sigma


    return z1,z2




matrix =  np.random.normal(0,1,(4096,4096))

print("done")
print(matrix)

eigvals, eigvecs = np.linalg.eig(matrix)

max_eig = np.amax(eigvals)

print(max_eig)

