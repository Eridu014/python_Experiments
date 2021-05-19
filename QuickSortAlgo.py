array1 = [3.18, 1.36, -0.12, 0.53, 1.92, 0.98, 45, 324729.45, -224, 0.000024,]

def quickSort(arr):
    less = []
    pivotList = []
    more = []

    if len(arr) <= 0:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more


print(quickSort(array1))