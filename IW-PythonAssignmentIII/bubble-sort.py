def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            # Driver code to test above


arr = [14,46,43,27,57,41,45,21,70]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i]),