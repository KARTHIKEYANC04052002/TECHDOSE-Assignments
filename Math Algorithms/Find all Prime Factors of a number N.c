#include <stdio.h>
#include <math.h>

int main()
{
    int i = 2, N;
    scanf("%d", &N);
    while(i <= sqrt(N)) {
        if(N % i == 0) {
            printf("%d ", i);
            N /= i;
        }
        else {
            i += 1;
        }
    }
    if(N > 1) printf("%d", N);
    return 0;
}