arr = [10, 20, 30, 40, 50, 60, 70, 80]
search = 0

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == search:
        print("Element Found")
        exit(0)
    elif arr[mid] < search:
        low = mid + 1
    else:
        high = mid - 1
print("Element Not Found")

# Time Complexity: O(log n)
# Space Complexity: O(1)