arr = [10, 60, 80, 50, 40]
search = 80

for i in range(len(arr)):
    if arr[i] == search:
        print("Element Found at index", i)
        exit(0)
print("Element Not Found")

# Time Complexity: O(n)
# Space Complexity: O(1)