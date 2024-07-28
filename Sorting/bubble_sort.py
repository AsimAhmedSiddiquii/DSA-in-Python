arr = [8, 6, 3, 2, 8, 1, 6, 2, 2]

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)

# Time Complexity: O(n^2)
# Space Complexity: O(1)