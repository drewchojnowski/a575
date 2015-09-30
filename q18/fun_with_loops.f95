!===================================================================
! OUTPUT:
!  [drewski@alphaboo q18]$ fun_with_loops
!     when x was                     1 , factorial was                     1
!     when x was                     3 , factorial was                     6
!     when x was                    13 , factorial was            6227020800
!     final x value:           12454041601
!     # of times the loop executed:                     3
!     sum of the factorials:            6227020807
!===================================================================

program fun_with_loops
    ! factorial-associated variables
    integer(8) :: i=2,nfac=1
    ! counters
    integer(8) :: y=0,iter_count=0
    ! variables
    integer(8) :: x=1,factorial_sum=0

    do while (x.le.100)
        if (x.lt.20) then
            y=x
            nfac=1
            do i=2, x
                nfac=nfac*i
            enddo
            x=nfac
            print *,'when x was ',y,', factorial was ',x
            factorial_sum=factorial_sum+x
        endif
        x=(x*2)+1
        iter_count=iter_count+1
    enddo

    print *,'final x value: ',x
    print *,'# of times the loop executed: ',iter_count
    print *,'sum of the factorials: ',factorial_sum
end
