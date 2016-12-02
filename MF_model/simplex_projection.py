import numpy as np

def euclidean_proj_simplex(v, s=1):
        n, = v.shape  # will raise ValueError if v is not 1-D
        if v.sum() == s and np.alltrue(v >= 0):
            return v
        u = np.sort(v)[::-1]
        cssv = np.cumsum(u)
        rho = np.nonzero(u * np.arange(1, n + 1) > (cssv - s))[0][-1]
        theta = (cssv[rho] - s) / (rho + 1.0)
        w = (v - theta).clip(min=0)
        return w
