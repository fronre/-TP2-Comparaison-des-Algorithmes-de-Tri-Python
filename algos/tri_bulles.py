def tri_bulles(lst):
    arr = list(lst)
    n = len(arr)
    if n < 2:
        return arr
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        n -= 1

    return arr


