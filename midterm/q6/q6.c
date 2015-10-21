#include<stdio.h>

int main() 
{
    int i, sum=0;
    for(i=1; i<=1000; i++)
        sum=sum+i;

    printf("sum of integers from 1 to 1000 is: %d\n",sum);

}

/* I verified the result by writing an IDL code to do the same thing.*/
