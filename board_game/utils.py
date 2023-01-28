import numpy as np

def which_direction(p1, p2):
    return np.array([p1[0]-p2[0], p1[1]-p2[1]])


def nearest_neighbor(contour, p_list, p_shape):
    sd = 1000000
    idx = [0]

    for i, pt in enumerate(p_list):
        d = (contour[-1][0] - pt[0]) ** 2 + (contour[-1][1] - pt[1]) ** 2
        if d < sd:
            sd = d
            idx = [i]
        elif d == sd:
            idx.append(i)

    if len(idx) > 0:
        for n in idx:
            direction = which_direction(p_list[n], contour[-1])
            if (direction == np.array([0, 1])).all():
                if p_shape[contour[-1][0], contour[-1][1]] == 1 and p_shape[contour[-1][0] -1, contour[-1][1]] == 0:
                    return n
            elif (direction == np.array([1, 0])).all():
                if p_shape[contour[-1][0], contour[-1][1]] == 0 and p_shape[contour[-1][0], contour[-1][1]-1] == 1:
                    return n
            elif (direction == np.array([0, -1])).all():
                if p_shape[contour[-1][0] - 1, contour[-1][1] - 1] == 1 and p_shape[contour[-1][0], contour[-1][1] - 1] == 0:
                    return n
            elif (direction == np.array([-1, 0])).all():
                if p_shape[contour[-1][0] - 1, contour[-1][1] - 1] == 0 and p_shape[contour[-1][0] - 1, contour[-1][1]] == 1:
                    return n

    else:
        return idx[0]