def merge(arr, low, mid, high):
    left_arr = arr[low : mid + 1]
    right_arr = arr[mid + 1 : high + 1]

    left_index = 0
    right_index = 0
    sorted_index = low

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] <= right_arr[right_index]:
            arr[sorted_index] = left_arr[left_index]
            left_index += 1
        else:
            arr[sorted_index] = right_arr[right_index]
            right_index += 1
        sorted_index += 1

    while left_index < len(left_arr):
        arr[sorted_index] = left_arr[left_index]
        left_index += 1
        sorted_index += 1

    while right_index < len(right_arr):
        arr[sorted_index] = right_arr[right_index]
        right_index += 1
        sorted_index += 1


def divide(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        divide(arr, low, mid)
        divide(arr, mid + 1, high)
        merge(arr, low, mid, high)


arr = [8, 6, 3, 2, 8, 1, 6, 2, 2]
divide(arr, 0, len(arr) - 1)
print(arr)

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
