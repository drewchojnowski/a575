import math

# OUTPUT:
#
#   drew@drewPC:~/a575/q18$ python fun_with_loops.py 
#   when x was  1 , factorial was  1
#   when x was  3 , factorial was  6
#   when x was  13 , factorial was  6227020800
#   final x value:  12454041601
#   # of times the loop executed:  3
#   sum of the factorials:  6227020807

x=1
iter_count=0
factorial_sum=0

while x <= 100:
    if x < 20:
        y=x
        x=math.factorial(x)
        print 'when x was ',y,', factorial was ',x
        factorial_sum=factorial_sum+x
    x=(x*2)+1
    iter_count=iter_count+1

print 'final x value: ',x
print '# of times the loop executed: ',iter_count
print 'sum of the factorials: ',factorial_sum
