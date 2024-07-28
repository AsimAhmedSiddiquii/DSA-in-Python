def partition(arr, low, high):
    l, h = low, high
    if low != high and low < high:
        pivot = arr[low]
        l += 1
        while(l <= h):
            if arr[h] < pivot and arr[l] > pivot:
                arr[h], arr[l] = arr[l], arr[h]
            if not arr[h] < pivot:
                h -= 1
            if not arr[l] > pivot:
                l += 1
    arr[h], arr[low] = arr[low], arr[h]
    return h

def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        print(arr)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot+1, high)

arr = [10, 16, 8, 12, 15, 6, 3, 9, 5]
quick_sort(arr, 0, len(arr)-1)

# Time Complexity: O(nlogn)
# Space Complexity: O(1)