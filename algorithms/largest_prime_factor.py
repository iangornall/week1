import math
def is_prime(num_in):
  # print num_in
  i = 2
  while i <= num_in ** 0.5:
    if num_in % i == 0:
      return False
    i += 1
  return True

def largest_prime_factor(num_in):
  i = 1
  while i <= num_in:
    if num_in % i == 0 and is_prime(num_in / i):
      return num_in / i
    i += 1

#print largest_prime_factor(600)
#print largest_prime_factor(13195)
print largest_prime_factor(600851475143)