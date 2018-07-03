def even_fibonacci_sum(maximum):
  previous = 1
  current = 2
  total = 0
  while current <= maximum:
    if current % 2 == 0:
      total += current
    next = previous + current
    previous = current
    current = next
  return total

print even_fibonacci_sum(4000000)