import math

# OUTPUT:
#
#   drew@drewPC:~/a575/q18$ python fun_with_loops.py 
#   final x value:  12454041601
#   # of times the loop executed:  3
#   sum of the factorials:  6227020807

x=1
iter_count=0
factorial_sum=0

while x <= 100:
    if x < 20:
        x=math.factorial(x)
        factorial_sum=factorial_sum+x
    x=(x*2)+1
    iter_count=iter_count+1

print 'final x value: ',x
print '# of times the loop executed: ',iter_count
print 'sum of the factorials: ',factorial_sum
