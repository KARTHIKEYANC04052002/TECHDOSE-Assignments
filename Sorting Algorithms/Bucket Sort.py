def insertion_sort(List):
    for i in range(1, len(List)):
        k = List[i]
        j = i - 1
        while j >= 0 and List[i] > k:
            List[i + 1] = List[i]
            j -= 1
        List[j + 1] = k
    return List
        
def bucket_sort(List, num_slots):
    Bucket = [[] for i in range(num_slots)]
    for val in List:
        ind = int(num_slots * val)
        Bucket[ind] += [val]
    for i in range(num_slots):
        Bucket[i] = insertion_sort(Bucket[i])
    Res = []
    for i in range(num_slots):
        Res += Bucket[i]
    return Res
    
L = [0.1, 0.2, 0.5, 0.3, 0.6, 0.8, 0.7]
print(bucket_sort(L, 10))