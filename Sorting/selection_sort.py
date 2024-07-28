arr = [8, 6, 3, 2, 8, 1, 6, 2, 2]

for i in range(len(arr)):
    min_index = i

    for j in range(i+1, len(arr)):
        if (arr[min_index] > arr[j]):
            min_index = j    
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)

# Time Complexity: O(n^2)
# Space Complexity: O(1)