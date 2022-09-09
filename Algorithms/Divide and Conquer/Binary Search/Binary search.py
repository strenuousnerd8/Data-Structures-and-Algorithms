def binarySearch(arr, low, high, data):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == data:
            return mid
        elif arr[mid] < data:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    arr = [20, 21, 39, 43, 49, 54, 73, 85, 96]
    n = len(arr)
    data = 20
    print(binarySearch(arr, 0, n - 1, data))