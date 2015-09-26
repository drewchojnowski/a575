pro fun_with_loops

; OUTPUT:
;
;   IDL> fun_with_loops   
;   final x value:    1.2454042e+10
;   # of times the loop executed:        3
;   sum of the factorials:    6.2270208e+09

x=LONG(1)
iter_count=0
factorial_sum=LONG(0)

if ~KEYWORD_SET(stop_at) then stop_at=100

while x le 100 do begin
    if x lt 20 then begin
        y=x
        x=factorial(x)
	print,'when x was ',y,', factorial was ',x
	factorial_sum=factorial_sum + x
    endif
    x=(x*2)+1
    iter_count=iter_count+1
endwhile

print,'final x value: ',x
print,'# of times the loop executed: ',iter_count
print,'sum of the factorials: ',factorial_sum

end
