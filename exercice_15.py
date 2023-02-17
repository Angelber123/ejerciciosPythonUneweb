# series de Fibonachi:
# la suma de dos elementos define el siguiente

a, b = 0, 1
# es lo mismo que esto:
# a = 0
# b = 1
while b < 10:
    print (b)
    # esto
    a, b = b, a+b
    # es lo mismo que esto:
    # a = b
    # b = a + b
