def insertionSort(l):
    for a in range(1, len(l)):
        b = a
        while b > 0 and l[b - 1] < l[b]:
            l[b - 1], l[b] = l[b], l[b - 1]
            b -= 1
            
def bucketSort(arr):
    n = len(arr)
    if n <= 0:
        return arr
    
    buckets = []
    for i in range(n):
        buckets.append([])
        
    max_value = max(arr)
    for i in range(n):
        index = num / (max_value + 1)
        bucketNumber = int(index * n)
        buckets[bucketNumber].append(arr[i])
        
    for bucket in buckets:
        insertionSort(bucket)
        
    output = []
    for bucket in buckets:
        output.extend(bucket)
    return output