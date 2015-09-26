pro fun_with_loops

; OUTPUT:
;
;   IDL> fun_with_loops
;   when x was            1, factorial was        1.0000000
;   when x was            3, factorial was        6.0000000
;   when x was           13, factorial was    6.2270208e+09

;   final x value:    1.2454042e+10
;   # of times the loop executed:        3
;   sum of the factorials:    6.2270208e+09

x=1
iter_count=0
factorial_sum=0

if ~KEYWORD_SET(stop_at) then stop_at=100

while x le 100 do begin
    if x lt 20 then begin
        y=x
        x=factorial(x)
	print,'when x was ',long(y),', factorial was ',x
	factorial_sum=factorial_sum + x
    endif
    x=(x*2)+1
    iter_count=iter_count+1
endwhile

print,'final x value: ',x
print,'# of times the loop executed: ',iter_count
print,'sum of the factorials: ',factorial_sum

end
