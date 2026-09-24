def compare_merge_quick_tasks(tasks):
  
    merge_count = 0
    quick_count = 0

    def before(a, b):
        if a[1] != b[1]:
            return a[1] > b[1]
        return a[0] < b[0]

    def merge_sort(arr):
        nonlocal merge_count

        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        result = []
        i = 0
        j = 0

        while i < len(left) and j <len(right):

            merge_count += 1

            if before(left[i], right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    def quick_sort(arr):
        nonlocal quick_count

        if len(arr) <= 1:
            return arr

        pivot = arr[-1]

        smaller = []
        greater = []

        for x in arr[:-1]:
            quick_count += 1

            if before(x, pivot):
                smaller.append(x)
            else:
                greater.append(x)

        return quick_sort(smaller) + [pivot] + quick_sort(greater)

    merge_result = merge_sort(tasks.copy())
    quick_result = quick_sort(tasks.copy())

    result = []

    result.append("Task Prioritization Report")

    result.append("Merge Sort Result")
    for task_id, priority in merge_result:
        result.append(f"{task_id} {priority}")

    result.append(f"Merge Comparisons: {merge_count}")

    result.append("Quick Sort Result")
    for task_id, priority in quick_result:
        result.append(f"{task_id} {priority}")

    result.append(f"Quick Comparisons: {quick_count}")

    if merge_count < quick_count:
        result.append("Better Algorithm: Merge Sort")
    elif quick_count < merge_count:
        result.append("Better Algorithm: Quick Sort")
    else:
        result.append("Better Algorithm: Both Equal")

    return result
