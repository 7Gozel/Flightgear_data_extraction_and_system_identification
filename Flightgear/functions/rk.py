

def runge_kutta_4th_order(x, dtt, u1, u2, a, b):
    dt2 = 0.5 * dtt

    xdt_temp = a @ x + b @ u1
    rk1 = xdt_temp * dt2

    u12 = (u1 + u2) / 2.0  # average of current and next inputs
    x1 = x + rk1
    xdt_temp_2 = a @ x1 + b @ u12
    rk2 = dt2 * xdt_temp_2

    x1 = x + rk2
    xdt_temp_3 = a @ x1 + b @ u12
    rk3 = dt2 * xdt_temp_3

    x1 = x + 2.0 * rk3
    xdt_temp_4 = a @ x1 + b @ u2
    rk4 = dt2 * xdt_temp_4

    x_f = x + (rk1 + 2.0 * (rk2 + rk3) + rk4) / 3.0

    return x_f


def runge_kutta_2nd_order(x, dt, u1, a, b):
    xdt_temp = a @ x + b @ u1
    k1 = xdt_temp * dt

    u12 = u1  # Using the same input for the midpoint calculation
    x1 = x + 0.5 * k1
    xdt_temp_2 = a @ x1 + b @ u12
    k2 = dt * xdt_temp_2

    x_f = x + k2

    return x_f
