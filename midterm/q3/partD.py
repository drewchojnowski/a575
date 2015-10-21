def func(x):
    f=(x**3)+(x**(2/3.))
    return f

# Example output, verified with calculator
#
# In [1]: import partA as a
#
# In [2]: print a.func(3)
# 29.0800838231
#
# In [3]: print a.func(4)
# 66.5198420998
#
# In [4]: print a.func(2)
# 9.58740105197

def simpson(a,b):
    a=float(a)
    b=float(b)
    p1=(b-a)/6.0
    p2=func(a)
    p3=4.0*(func(a+b)/2.0)
    p4=func(b)
    result=p1 * (p2 + p3 + p4)
    
    return result

# Example output, verified with calculator
#
# In [4]: print a.simpson(1,2)
# 11.624594783
#
# In [7]: print a.simpson(1,3)
# 54.7065893409

def func2(x):
    f=((1/4.0)*(x**4))+((3/5.0)*(x**(5/3.0)))
    return f

# Example output, verified with calculator
#
# In [1]: import partC as a
#
# In [2]: print a.func2(10)
# 2527.849533

# this is pretty far off from the partC result.
# partD result/partC result = 0.50323



