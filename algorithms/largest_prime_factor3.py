def largest_prime_factor(num):
  remainder = num
  factor = 2
  while remainder != 1:
    if remainder % factor == 0:
      remainder /= factor
    else:
      factor += 1
  
  return factor

# when remainder = 1

#print largest_prime_factor(600)
#print largest_prime_factor(13195)
#print largest_prime_factor(600851475143)
print largest_prime_factor(13)
