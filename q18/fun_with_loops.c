#include<stdio.h>

/* OUTPUT:
drew@drewPC:~/a575/q18$ ./fun_with_loops 
   when x was 1, factorial was 1
   when x was 3, factorial was 6
   when x was 13, factorial was 1932053504
   final x value: 3864107009
   # of times the loop executed: 3
   sum of the factorials: 1932053511
*/

/* NOTE:
I'm not quite sure why this isn't working, i.e. why the value of get_factorial(13) is wrong.
I experimented with data types to try and remedy this, but did not succeed.
*/

int main() 
{
    int i;
    unsigned long long int x=1;
    int y=0;
    int iter_count=0;
    unsigned long long int factorial_sum=0;

    while (x <= 100) {
        if (x < 20) {
            y=x;
            x=get_factorial(x);
            printf("when x was %d, factorial was %llu\n",y,x);
            factorial_sum=factorial_sum+x;
        }
        x=(x*2)+1;
        iter_count=iter_count+1;
    }

    // this is a simple C program

    printf("final x value: %llu\n",x);
    printf("# of times the loop executed: %d\n",iter_count);
    printf("sum of the factorials: %llu\n",factorial_sum);

}

int get_factorial(int x)
{
    int i, f=1;
 
    for(i=1;i<=x;i++)
        f=f*i;
 
     return f;
}
