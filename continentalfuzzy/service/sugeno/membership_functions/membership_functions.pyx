from libc.math cimport exp

def c_calculate_gaussmf(double x, double mean, double sigma):
    return exp(-((x - mean) * (x - mean)) / (2.0 * sigma * sigma))