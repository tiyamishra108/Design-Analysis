def compare_bubble_insertion(random_data, sorted_data, reverse_data):
    result = ["Sorting Performance Report"]

    datasets = [
        ("Random Dataset", random_data),
        ("Sorted Dataset", sorted_data),
        ("Reverse Dataset", reverse_data)
    ]

    for name, data in datasets: 
      
      bubble = data[:]
      bubble_comparisons = 0
      bubble_swaps = 0

      n = len(bubble)

      for i in range(n - 1):
          swapped = False
        
          for j in range(n - 1 - i):
              bubble_comparisons += 1

              if bubble[j] > bubble[j + 1]:
                  bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]
                  bubble_swaps += 1
                  swapped = True

          if not swapped:
              break

      insertion = data[:]
      insertion_comparisons = 0
      insertion_shifts = 0

      for i in range(1, n):
          key = insertion[i]
          j = i - 1

          while j >= 0:
             insertion_comparisons += 1

             if insertion[j] > key:
                 insertion[j +1] = insertion[j]
                 insertion_shifts += 1
                 j -= 1
             else: 
                 break

          insertion[j + 1] = key

      if bubble_comparisons < insertion_comparisons:
          better = "Bubble Sort"
      elif insertion_comparisons < bubble_comparisons:
          better = "Insertion Sort"
      else:
          better = "Both Equal"

      result.append(name)
      result.append("Bubble Sorted: " + " ".join(map(str, bubble)))
      result.append("Bubble Comparisons: " + str(bubble_comparisons))
      result.append(f"Bubble Swaps: " + str(bubble_swaps))
      result.append("Insertion Sorted: " + " ".join(map(str, insertion)))
      result.append(f"Insertion Comparisons: " + str(insertion_comparisons))
      result.append(f"Insertion Shifts: " + str(insertion_shifts))
      result.append(f"Better Algorithm: " + better)

    return result