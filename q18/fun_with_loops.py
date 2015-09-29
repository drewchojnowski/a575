import math

#===================================================================
# OUTPUT:
#
#   drew@drewPC:~/a575/q18$ python fun_with_loops.py 
#   when x was  1 , factorial was  1
#   when x was  3 , factorial was  6
#   when x was  13 , factorial was  6227020800
#   final x value:  12454041601
#   # of times the loop executed:  3
#   sum of the factorials:  6227020807
#===================================================================

# VARIABLES:
x=1
xmax=100
do_factorial_limit=20
x_multiply=2
x_add=1

#COUNTERS:
iter_count=0
factorial_sum=0

while x <= xmax:
    if x < do_factorial_limit:
        y=x
        x=math.factorial(x)
        print 'when x was ',y,', factorial was ',x
        factorial_sum=factorial_sum+x
    x=(x*x_multiply)+x_add
    iter_count=iter_count+1

print 'final x value: ',x
print '# of times the loop executed: ',iter_count
print 'sum of the factorials: ',factorial_sum
