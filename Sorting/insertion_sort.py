arr = [3, 6, 8, 2, 8, 1, 6, 2, 2]

for i in range(1, len(arr)):
    key = arr[i]
    
    j = i-1
    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key

print(arr)

# Time Complexity: O(n^2)
# Space Complexity: O(1)