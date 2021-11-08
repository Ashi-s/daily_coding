from random import random
from math import sqrt


def getPiValue():
    
    # lets understand the equation
    # lets take a square(1x1) and draw a quarter in it
    # area of square = r**2 = 1 = S
    # area of quarter = pi x r**2 / 4 = pi x S / 4
    # if we draw a large number of dots inside the square
    # and lets call number of the dots inside quarter = I
    # and total number of dots inside the sqaure
    # we can say that (I / N) = (area of quarter / area of square)
    # (I / N) = (pi x S)/4  /  S
    # pi = (4 * I) / N
    
    N = 100000 # higher the value more acurate the PI result
    I = 0
    for i in range(N):
        x = random() #random between 0 & 1
        y = random() #random between 0 & 1
        
        #check if dot is inside the quarter(circle)
        r = sqrt(x**2 + y**2)
        if r <= 1:
            I += 1
        
    pi = (4 * I) / N
    
    return pi
    
print(getPiValue())
        
    
    