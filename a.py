import math #use the function tan() and pi

def polysum(n,s):
    '''
    n:positive integer
    s:positive number
   
    returns:sum the area and square of the perimeter
            of the regular polygan and rounded to 4 
            decimal places.
    '''
    area = 0.25 * n * s * s / (math.tan(math.pi / n))
    perimeter = n * s
    return round(area + perimeter*perimeter,4) #rounded to 4 decimal
    