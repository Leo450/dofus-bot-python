import basic_colormath


def similar(c1, c2, threshold=1):
    return basic_colormath.get_delta_e(c1, c2) < threshold