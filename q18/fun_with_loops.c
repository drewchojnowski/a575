/*=============================================
OUTPUT:
    drew@drewPC:~/a575/q18$ ./fun_with_loops 
    when x was 1, factorial was 1.000000
    when x was 3, factorial was 6.000000
    when x was 7, factorial was 5040.000000
    when x was 15, factorial was 1307674279936.000000
    final x value: 127
    # of times the loop executed: 6
    sum of the factorials: 1307674279936.000000
=============================================*/
#include<stdio.h>

int main() 
{
    float f=1, factorial_sum=0;
    int i, x=1, xmax=100, do_factorial_limit=20, x_multiply=2, x_add=1, iter_count=0;

    while (x <= xmax) {
        if (x < do_factorial_limit) {
            for(i=1; i<=x; i++)
                f=f*i;
            printf("when x was %d, factorial was %f\n",x,f);
            factorial_sum=factorial_sum+f;
            f=1;
        }
        x=(x*x_multiply)+x_add;
        iter_count++;
    }

    printf("final x value: %d\n",x);
    printf("# of times the loop executed: %d\n",iter_count);
    printf("sum of the factorials: %f\n",factorial_sum);

}

