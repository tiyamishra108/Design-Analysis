def generate_runtime_chart_report(sizes):
    result = []

    result.append("Runtime Comparison Chart Data")
    result.append("InputSize LinearSearch BinarySearch BubbleSort InsertionSort")

    for n in sizes:
        linear_search = n
        binary_num = 0
        temp = n

        while temp > 1:
            temp //= 2
            binary_num += 1

        binary_search = binary_num + 1

        # Bubble Sort = n * (n - 1) / 2
        bubble_sort = n * (n - 1) // 2

        # Insertion Sort = n * (n - 1) / 2
        insertion_sort = n * (n - 1) // 2

        result.append(
            f"{n} {linear_search} {binary_search} "
            f"{bubble_sort} {insertion_sort}"
        )

    result.append("Scalability Summary")
    result.append("Algorithm Complexity Scalability")
    result.append("Linear Search O(n) Moderate")
    result.append("Binary Search O(log n) Excellent")
    result.append("Bubble Sort O(n^2) Poor")
    result.append("Insertion Sort O(n^2) Poor")

    result.append("Key Observations")
    result.append("Best Algorithm: Binary Search")
    result.append("Most Expensive Algorithm: Bubble Sort")
    result.append("Conclusion: Logarithmic algorithms scale better for large inputs")

    return result