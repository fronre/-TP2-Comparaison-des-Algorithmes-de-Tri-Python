def tri_echange(lst):
    """Exchange sort implemented as an in-place quicksort wrapper that returns a new list.

    The name 'tri_echange' is interpreted here as an exchange-based sort; quicksort is used for reasonable performance.
    """
    arr = list(lst)

    def _quicksort(a, lo, hi):
        if lo < hi:
            p = _partition(a, lo, hi)
            _quicksort(a, lo, p - 1)
            _quicksort(a, p + 1, hi)

    def _partition(a, lo, hi):
        pivot = a[hi]
        i = lo
        for j in range(lo, hi):
            if a[j] <= pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[hi] = a[hi], a[i]
        return i

    _quicksort(arr, 0, len(arr) - 1)
    return arr
