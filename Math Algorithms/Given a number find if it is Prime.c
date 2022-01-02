#include <stdio.h>
#include <math.h>
#include <stdbool.h>

int main()
{
    int i, N, flag;
    scanf("%d", &N);
    flag = true;
    for(i=2; i<=sqrt(N); i++) {
        if(N % i == 0) {
            flag = false;
            break;
        }
    }
    printf("%d %s", N, flag == true ? "is Prime." : "is not Prime");
    return 0;
}