from sympy import symbols, integrate, I, diff, exp, pi

x, y, t, r, theta = symbols("x y t r theta", real=True)


def path1():  # 积分路径 y=0
    x = t
    y = 0
    z = x + I * y
    dzdt = diff(z, t)
    return integrate(z * dzdt, (t, 0, 1))


def path2():  # 积分路径 x=1
    x = 1
    y = t
    z = x + I * y
    dzdt = diff(z, t)
    return integrate(z * dzdt, (t, 0, 1))


def path3():  # 积分路径 y=1
    x = t
    y = 1
    z = x + I * y
    dzdt = diff(z, t)
    return integrate(z * dzdt, (t, 1, 0))


def path4():  # 积分路径 x=0
    x = 0
    y = t
    z = x + I * y
    dzdt = diff(z, t)
    return integrate(z * dzdt, (t, 1, 0))


def path_integral_holomorphic():
    print("积分路径 y=0: "+str(path1()))
    print("积分路径 x=1: "+str(path2()))
    print("积分路径 y=1: "+str(path3()))
    print("积分路径 x=0: "+str(path4()))
    print("和: "+str(path1() + path2() + path3() + path4()))


def path_integral():
    z = 1+r*exp(theta*I)
    dzdtheta = diff(z, theta)
    f = 1/(z-1)
    return integrate(f*dzdtheta, (theta, 0, 2*pi))


def path_integral_non_holomorphic():
    print("f=1/(z-1) 圆的曲线积分: "+str(path_integral()))


# Test 1: holomorphic function
path_integral_holomorphic()
# Test 2: non-holomorphic function
path_integral_non_holomorphic()
