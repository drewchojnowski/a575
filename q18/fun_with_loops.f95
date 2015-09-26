! This program does not work !

module fact_mod
contains
    function factorial(x)
        integer :: i,x
        real (kind(1.0d0)) :: factorial
        factorial=1
        do i=2,x
            factorial=factorial*i
        enddo
    end function
end module

program fun_with_loops
    use fact_mod
    ! this is a comment

    integer :: x,y,iter_count
    x=1
    y=0
    iter_count=0

    do while (x <= 100)
        if (x < 20) then
            y=x
            x=factorial(x)
            print *,'when x was ',y,', factorial was ',x
        end if
        x=(x*2)+1
        iter_count=iter_count+1
    enddo

    print *,'final x value: ',x
    print *,'# of times the loop executed: ',iter_count
    print *,'sum of the factorials: ',factorial_sum

end
