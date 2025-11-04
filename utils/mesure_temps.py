import time

def mesurer_temps(sort_func, arr):
    """Measure execution time of sort_func when called with arr.

    Returns (elapsed_seconds, sorted_result)
    """
    start = time.perf_counter()
    # Call with a copy to avoid mutating caller's data if function sorts in-place
    result = sort_func(list(arr))
    end = time.perf_counter()
    return end - start, result
