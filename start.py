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



print ("test")

#a = 11
#if a == 10:
  #  print ("a = 10")
#else:
 #   print ("a != 10")


# summa a , from 1 to 1000
a = 0
for x in range(1000):
  print(x+1)
  a = a +(x+1)
print("first result: " + str(a))

b = function_summa(1000, 1 )
print ("second result: " + str(b))


for x in range(1000):
    b = function_summa(x, 0)
    print("second result: " + str(b))
################################################

horizontal_value = 4
vertical_value = 5
flat_value = horizontal_value * vertical_value
print("third result: " + str(flat_value))

flat_value = flat_calculation (horizontal_value , vertical_value)
print("third result: " + str(flat_value))

circuit_value = circuit_calculation (horizontal_value , vertical_value)
print("fourth result: " + str(circuit_value))

x, y = squia_calculation(horizontal_value, vertical_value)

print("perim result: " + str(x) + " flat result: " + str(y))

##############################################
# perimetr kruga flat kruga


r_value = 3
s_value = r_value * r_value * math.pi
print("s_value:" + str(s_value))
o_value = 2 * r_value * math.pi
print("o_value:" + str(o_value))

r_value = 4
s_value = r_value * r_value * math.pi
print("s_value:" + str(s_value))
o_value = 2 * r_value * math.pi
print("o_value:" + str(o_value))

r_value = 5
s_value = r_value * r_value * math.pi
print("s_value:" + str(s_value))
o_value = 2 * r_value * math.pi
print("o_value:" + str(o_value))

x = 3
a,b = circle_calculation(x)
print(a,b)

