def fib2(n): #devuelve la serie de Fibonacci hasta n
    """Devuelve una lista conteniendo la serie de Fibonacci"""
    result = []
    a, b =0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
        return result


        f10 = fib2(10)
        print(f10)
        