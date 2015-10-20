;===================================================================
; OUTPUT:
;   IDL> fun_with_loops
;   when x was            1, factorial was        1.0000000
;   when x was            3, factorial was        3.0000000
;   when x was            7, factorial was        5040.0000
;   when x was           15, factorial was    1.3076744e+12
;   final x value:      127
;   # of times the loop executed:        6
;   sum of the factorials:    1.3076744e+12
;===================================================================
pro fun_with_loops

; VARIABLES:
x=1
xmax=100
do_factorial_limit=20
x_multiply=2
x_add=1

; COUNTERS
iteration_count=0
factorial_sum=0

while x le xmax do begin
    if x lt do_factorial_limit then begin
        y=factorial(x)
	print,'when x was ',x,', factorial was ',y
	factorial_sum=factorial_sum + y
    endif
    x=(x*x_multiply)+x_add
    iteration_count=iteration_count+1
endwhile

print,'final x value: ',x
print,'# of times the loop executed: ',iteration_count
print,'sum of the factorials: ',factorial_sum

end
