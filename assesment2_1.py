def analyze_recursive_iterative(n):
  
   def recursive_factorial(x):
      if x == 0:
          return 1
      return x * recursive_factorial(x-1)

   def iterative_factorial(x):
      result = 1
      for i in range(1, x + 1):
          result *= i
      return result

   def recursive_fibonacci(x):
     if x == 0:
         return 0 
     if x == 1:
         return 1 
     return recursive_fibonacci(x - 1) + recursive_fibonacci(x - 2)

   def iterative_fibonnaci(x):
      if x == 0:
          return 0
      if x == 1:
          return 1

      a = 0
      b = 1

      for i in range(2, x + 1):
          c = a + b
          a = b
          b = c

      return b

      recursive_fact = recursive_factorial(n)
      iterative_fact = iterative_factorial(n)
      recursive_fib = recursive_fibonacci(n)
      iterative_fib = iterative_fibonnaci(n)

      recursive_fact_count = n + 1
      iterative_fact_count = n 
      iterative_fib_count = n
      recursive_fib_count = n

      def fib_call_count(x):
          if x == 0 or x == 1:
              return 1
          return 1 + fib_call_count(x - 1) + fib_call_count(x - 2)

      recursive_fib_count = 1
      a = 1
      b = 1
      for i in range(2, n + 1):
          recursive_fib_count = 1 + a + b
          a = b
          b = recursive_fib_count

   return[
        "Computation Analysis Report",
        f"Recursive Factorial: {recursive_factorial(n)}",
        f"Iterative Factorial: {iterative_factorial(n)}",
        f"Recursive Fibonacci: {recursive_fibonacci(n)}",
        f"Iterative Fibonacci: {iterative_fibonnaci(n)}",
        "Operation Count Comparison",
        f"Recursive Factorial Count: {n + 1}",
        f"Iterative Factorial Count: {n}",
        f"Recursive Fibonacci Count: {2 * recursive_fibonacci(n + 1) - 1}",
        f"Iterative Fibonacci Count: {n}"
]