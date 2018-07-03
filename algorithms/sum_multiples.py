def sum_multiples(number_in):
  sum = 0
  for num in range(number_in):
    if num % 3 == 0 or num % 5 == 0:
      sum += num
  return sum

print sum_multiples(1000)