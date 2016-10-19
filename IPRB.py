def f(x,y,z):
    s = x+y+z #the sum of population
    c = s*(s-1)/2.0 #comb(2,s)
    p = 1 - (z*(z-1)/2+0.25*y*(y-1)/2+y*z*0.5)/c
    return p

print f(2,2,2)