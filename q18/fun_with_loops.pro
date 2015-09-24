pro fun_with_loops

; output:
;  IDL> fun_with_loops
;  # of times the loop executed:        3
;  sum of the factorials:    6.2270208e+09

x=1
count=0
y=0
while x le 100 do begin
    if x lt 20 then begin
        x=factorial(x)
	y=y+x
    endif
    x=(x*2)+1
    count=count+1
endwhile

print,'# of times the loop executed: ',count
print,'sum of the factorials: ',y

end
