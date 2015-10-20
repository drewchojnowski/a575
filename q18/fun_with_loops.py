#===================================================================
# OUTPUT:
#   drew@drewPC:~/a575/q18$ python fun_with_loops.py 
#   when x was  1 , factorial was  1
#   when x was  3 , factorial was  6
#   when x was  7 , factorial was  5040
#   when x was  15 , factorial was  1307674368000
#   final x value:  127
#   of times the loop executed:  6
#   sum of the factorials:  1307674373047
#===================================================================
import math

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
        y=math.factorial(x)
        print 'when x was ',x,', factorial was ',y
        factorial_sum=factorial_sum+y
    x=(x*x_multiply)+x_add
    iter_count=iter_count+1

print 'final x value: ',x
print '# of times the loop executed: ',iter_count
print 'sum of the factorials: ',factorial_sum
