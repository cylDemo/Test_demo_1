def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("排序后的数组为为：")
    for i in range(len(arr)):
        print("%d" %arr[i])

arr = [56, 25, 78, 32, 14, 69, 54, 65, 98, 12, 24]
bubble_sort(arr)