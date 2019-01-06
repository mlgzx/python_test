import math


def function_summa(value, shift):
    local_summ = 0
    for x in range(value):
        local_summ = local_summ + (x + shift)
    return local_summ


def circuit_calculation(horizontal_value, vertical_value):
    local_value = horizontal_value*2 + vertical_value*2

    return local_value


def flat_calculation(horizontal_value, vertical_value):
    local_value = horizontal_value * vertical_value

    return local_value


def squia_calculation(horizontal_value, vertical_value):
    local_perimetr = horizontal_value*2 + vertical_value*2
    local_flat = horizontal_value * vertical_value
    return local_perimetr,local_flat


def circle_calculation(r_value):
    s_value = r_value * r_value * math.pi
    o_value = 2 * r_value * math.pi
    return o_value,s_value
