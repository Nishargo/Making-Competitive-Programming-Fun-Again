# Prime number: A number is called a prime number if it has 2 factors including the number itself and 1. It's a natural number greater than 1. 
# 3 is a prime number because we get 3 as a product, either 1 × 3 or 3 × 1, involving 3 itself

def check_if_it_is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True
  
print(f'{check_if_it_is_prime(13)}')
