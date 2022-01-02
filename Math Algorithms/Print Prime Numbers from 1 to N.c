#include <stdio.h>
#include <math.h>
#include <stdbool.h>

int main()
{
    int i, j, N, flag;
    scanf("%d", &N);
    for(i=2; i<N; i++) {
        flag = true;
        for(j=2; j<=sqrt(i); j++) {
            if(i % j == 0) {
                flag = false;
                break;
            }
        }
        if(flag == true) {
            printf("%d ", i);
        }
    }
    return 0;
}