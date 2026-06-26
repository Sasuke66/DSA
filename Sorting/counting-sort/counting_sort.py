def countingSort(arr):
    max_element = max(arr)
    
    count = [0] * (max_element + 1)
    
    for num in arr:
        count[num] += 1
    
    arr[:] = []
    
    
    for num, freq in enumerate(count):
        arr.extend([num] * freq)
        
    return arr