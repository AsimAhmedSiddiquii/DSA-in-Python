arr = [10, 20, 30, 40, 50, 60, 70, 80]
search = 20

low = 0
high = len(arr) - 1

def binary_search(low, high):
    if low <= high:
        mid = (high + low) // 2
        print(mid)
        if arr[mid] == search:
            return True
        elif arr[mid] < search:
            return binary_search(mid+1, high)
        else:
            return binary_search(low, mid-1)
    else:
        return False

print(binary_search(low, high))

# Time Complexity: O(log n)
# Space Complexity: O(1)