def fibonacci(n):
    """
    A function to get the nth fibonacci number
    """
    #Base Case
    #to get the first two elements of the series 0,1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """
    A function to get the nth lucas number
    """
    #Base Case
    #to get the first two elements of the series 2,1
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

def sum_series(n, para1=0, para2=1):
    """
    A function to get the nth fibonacci number or lucas number based on the arguments. Enter (n,2,1) to get lucas number. Enter (n) to get fibonacci number.
    """
        #Base Case
    if n == 0:
        return para1
    elif n == 1:
        return para2
    else:
        return sum_series(n - 1, para1, para2) + sum_series(n - 2, para1, para2)