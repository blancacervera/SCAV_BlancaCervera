from scipy.fftpack import dct


def discrete_function(array):
    x = dct(array)
    print(x)