def minDiff(L, stu_count):
    N = len(L)
    L.sort()
    start, end = 0, stu_count - 1
    min_diff = L[end] - L[start]
    while end < N - 1:
        start += 1
        end += 1
        X = L[end] - L[start]
        if X < min_diff:
            min_diff = X
    return min_diff

# L, stu_count = list(map(int, input().split())), int(input())
L = [12, 4, 7, 9, 2, 23, 25, 41,
          30, 40, 28, 42, 30, 44, 48, 
          43, 50]
stu_count = 7
print(minDiff(L, stu_count))