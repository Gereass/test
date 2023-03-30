import numpy as np


def calc_fun(x):
    f = (np.cos(x) ** 2) - (2 * x)
    return f


def calc_min(Fu, Xu):
    fmin = min(Fu)
    xmin = Xu[Fu.index(fmin)]
    O = [fmin, xmin]
    return (O)


def calc_p_min(x1_m, x2_m, x3_m, fx1_m, fx2_m, fx3_m):
    return ((x2_m * x2_m - x3_m * x3_m) * fx1_m + (x3_m * x3_m - x1_m * x1_m) * fx2_m +
            (x1_m * x1_m - x2_m * x2_m) * fx3_m) / \
           (2 * (x2_m - x3_m) * fx1_m + (x3_m - x1_m) * fx2_m + (x1_m - x2_m) * fx3_m)


def main():
    print('determination of the minimum of the functon by the '
          'method of quadratic interpolation:cos(x)^2-(2*x)')

    x1 = round(float(input('enter start point, x1=')), 6)
    dx = round(float(input('enter value step dx=')), 6)
    e1 = round(float(input('enter enter accuracy e1=')), 6)
    e2 = round(float(input('enter enter accuracy e2= ')), 6)
    flag = 0
    flag2 = 0

    while flag != 1:
        x2 = round(x1 + dx, 6)
        fx1 = round(calc_fun(x1), 6)
        fx2 = round(calc_fun(x2), 6)
        if fx1 > fx2:
            x3 = round(x1 + 2 * dx, 6)
        if fx1 < fx2:
            x3 = round(x1 - dx, 6)
        fx3 = round(calc_fun(x3), 6)
        F = [fx1, fx2, fx3]
        X = [x1, x2, x3]
        A = calc_min(F, X)
        flag2 = 0

        while flag2 != 1:

            fmin = round(A[0], 6)
            xmin = round(A[1], 6)

            if 2 * (x2 - x3) * fx1 + (x3 - x1) * fx2 + (x1 - x2) * fx3 == 0:
                x1 = round(xmin, 6)

                flag = 0
                flag2 = 1
            else:
                p_x_min = round((calc_p_min(x1, x2, x3, fx1, fx2, fx3)), 6)
                p_f_min = round(calc_fun(p_x_min), 6)

                if abs((fmin - p_f_min) / p_f_min) < e1 and abs((xmin - p_x_min) / p_x_min) < e2:
                    print('required minimum: ', p_x_min)
                    flag = 1
                    flag2 = 1
                else:
                    m = abs((fmin - p_f_min) / p_f_min)
                    n = abs((xmin - p_x_min) / p_x_min)

                    if (x1 <= p_x_min) or (p_x_min >= x2):
                        if m > e1 or n > e2:
                            X.append(p_x_min)
                            X.append(xmin)
                            F.append(p_f_min)
                            F.append(fmin)
                            R = X
                            R.sort()
                            i = 0
                            flag3 = 0
                            # delet excess element in R
                            while flag3 != 1:
                                if R[i] == R[i + 1]:
                                    del R[i]
                                    flag3 = 1
                                else:
                                    i += 1
                            # #  choose and enter the best point then enter befor and after point
                            # for ss in range(len(R)):
                            #     if abs(p_x_min)<abs(xmin) and p_x_min!=R[3]:
                            #         x2=p_x_min
                            #         pre_x1=R.index(x2)
                            #         x1=R[pre_x1-1]
                            #         pre_x3 = R.index(x2)
                            #         x3 = R[pre_x3+1]
                            #     else:
                            #         if abs(p_x_min) > abs(xmin) and xmin != R[3]:
                            #             x2 = xmin
                            #             pre_x1 = R.index(x2 )
                            #             x1 = R[pre_x1-1]
                            #             pre_x3 = R.index(x2)
                            #             x3 = R[pre_x3+1]
                            print('choose and enter the best point p_x_min(', p_x_min, ') or xmin(', xmin,
                                  ') then enter befor and after point', R)
                            x2 = round(float(input()), 6)
                            x1 = round(float(input()), 6)
                            x3 = round(float(input()), 6)

                            F = [F[X.index(x1)], F[X.index(x2)], F[X.index(x3)]]
                            X = [x1, x2, x3]
                            fx1 = round(F[0], 6)
                            fx2 = round(F[1], 6)
                            fx3 = round(F[2], 6)

                            A = calc_min(F, X)

                            flag2 = 0
                        else:
                            x1 = round(p_x_min, 6)
                            flag2 = 1
                            flag = 0
                            break
                    else:
                        x1 = round(p_x_min, 6)
                        flag2 = 1
                        flag = 0
                        break


if __name__ == '__main__':
    main()
