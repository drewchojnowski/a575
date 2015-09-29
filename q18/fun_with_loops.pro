pro fun_with_loops

;===================================================================
; OUTPUT:
;
;   IDL> fun_with_loops
;   when x was            1, factorial was        1.0000000
;   when x was            3, factorial was        6.0000000
;   when x was           13, factorial was    6.2270208e+09

;   final x value:    1.2454042e+10
;   # of times the loop executed:        3
;   sum of the factorials:    6.2270208e+09
;===================================================================

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
        y=x
        x=factorial(x)
	print,'when x was ',long(y),', factorial was ',x
	factorial_sum=factorial_sum + x
    endif
    x=(x*x_multiply)+x_add
    iteration_count=iteration_count+1
endwhile

print,'final x value: ',x
print,'# of times the loop executed: ',iteration_count
print,'sum of the factorials: ',factorial_sum

end
