def generate_execution_observation_table(sizes):
    
    fib_calls = [1] * 35
    for i in range(2, 35):
        fib_calls[i] = 1 + fib_calls[i - 1] + fib_calls[i - 2]

    
    print("Algorithm Execution Observation Table")
    print("InputSize RecursiveFactorial IterativeFactorial RecursiveFibonacci IterativeFibonacci LinearSearch BinarySearch BubbleSort InsertionSort")

    for n in sizes:
        rec_factorial = n + 1
        iter_factorial = n
        rec_fibonacci = fib_calls[n]
        iter_fibonacci = n
        linear_search = n

        binary_search = 0
        x = n
        while x > 0:
            binary_search += 1
            x //= 2

        bubble_sort = n * (n - 1) // 2
        insertion_sort = n * (n - 1) // 2

        print(f"{n} {rec_factorial} {iter_factorial} {rec_fibonacci} {iter_fibonacci} {linear_search} {binary_search} {bubble_sort} {insertion_sort}")

    return []