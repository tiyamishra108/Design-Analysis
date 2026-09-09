def generate_runtime_complexity_table(n):
    result = []

    result.append("Runtime Complexity Comparison")
    result.append("Method ObservedCount ExpectedComplexity Observation")

    result.append(f"Linear Search {n} O(n) Grows linearly")

   
    count = 0
    temp = n
    while temp > 0:
        count += 1
        temp //= 2

    result.append(f"Binary Search {count} O(log n) Grows logarithmically")

    sort_count = n * (n - 1) // 2

    result.append(f"Bubble Sort {sort_count} O(n^2) Grows quadratically")
    result.append(f"Insertion Sort {sort_count} O(n^2) Grows quadratically")

    return result