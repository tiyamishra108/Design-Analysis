def compare_search_algorithms(arr, target):
    linear_index = -1
    linear_comparisons = 0

    for i in range(len(arr)):
        linear_comparisons += 1
        if arr[i] == target:
            linear_index = i
            break

    low = 0 
    high = len(arr) - 1
    binary_index = -1
    binary_comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        binary_comparisons += 1

        if arr[mid] == target:
           binary_index = mid
           high = mid - 1
        elif arr[mid] < target:
          low = mid + 1
        else:
          high = mid - 1

    if linear_comparisons < binary_comparisons:
        better = 'Linear Search'
    elif binary_comparisons < linear_comparisons:
          better = 'Binary Search'
    else:
         better = 'Both Equal'

    return[
        "Search Comparison Report",
        "Linear Search",
        f"Index: {linear_index}",
        f"Comparisons: {linear_comparisons}",
        "Binary Search",
        f"Index: {binary_index}",
        f"Comparisons: {binary_comparisons}",
        f"Better Algorithm: {better}"
    ]