#include <stdio.h>

int main()
{
    long long int X, Y, res=1;
    scanf("%lld %lld", &X, &Y);
    while(Y > 0) {
        if(Y % 2 == 1) {
            res *= X;
        }
        X *= X;
        Y /= 2;
    }
    printf("%lld", res);
    return 0;
}