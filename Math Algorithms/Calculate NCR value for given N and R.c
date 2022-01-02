#include <stdio.h>

int gcd(int x, int y) {
	if(x == 0) return y;
	gcd(y % x, x);
}

int main() {
	int n, r;
	printf("Enter value of N : ");
	scanf("%d", &n);
	printf("Enter value for R : ");
	scanf("%d", &r);
	if(n - r < r) r = n - r;
	int p = 1, k = 1, g;
	if(r > 0) {
		while(r > 0) {
			p *= n;
			k *= r;
			g = gcd(g, k);
			p /= g;
			k /= g;
			n--;
			r--;
		}
	}
	printf("Answer = %d", p/k);
}