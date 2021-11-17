def rgb_to_yuv(r, g, b):  # rgb to yuv conversion following the theoretical video given
    y = (0.257 * r) + (0.504 * g) + (0.098 * b) + 16
    u = (-0.148 * r) - (0.291 * g) + (0.439 * b) + 128
    v = (0.439 * r) - (0.368 * g) - (0.071 * b) + 128
    y = int(y)  # we get an integer number for the color value
    u = int(u)
    v = int(v)
    print(y, u, v)
    return


def yuv_to_rgb(y, u, v):  # yuv to rgb conversion following the theoretical video given
    r = 1.164 * (y - 16) + 1.596 * (v - 128)
    g = 1.164 * (y - 16) - 0.813 * (v - 128) - 0.391 * (u - 128)
    b = 1.164 * (y - 16) + 2.018 * (u - 128)
    r = int(r)   # we get an integer number for the color value
    g = int(g)
    b = int(b)
    print(r, g, b)
    return


