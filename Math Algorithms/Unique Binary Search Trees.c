
int numTrees(int n){
    long long int res = 1, i;
    for(i=1; i<=n; i++) {
        res *= (4 * i - 2);
        res /= (i + 1);
    }
    return (int)res;
}