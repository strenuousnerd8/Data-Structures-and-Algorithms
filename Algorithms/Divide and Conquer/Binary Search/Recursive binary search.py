def recursiveBinarySearch(arr, low, high, data):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == data:
        return mid
    elif arr[mid] < data:
        return recursiveBinarySearch(arr, mid + 1, high, data)
    else:
        return recursiveBinarySearch(arr, low, mid - 1, data)

if __name__ == "__main__":
    arr = [20, 21, 39, 43, 49, 54, 73, 85, 96]
    n = len(arr)
    data = 49
    print(recursiveBinarySearch(arr, 0, n - 1, data))