things = ['apples', 'baboons', 'cribs', 'dulcimers']

# What is the efficiency of this algorithm?
for thing in things:
  print("Here's a thing: %s" % thing)

# Prime Algorithm - Any whole number above 1 that can only be divided by itself.
def is_prime(number):
  for i in range(2, number):
    if number % i == 0:
      print('False')
      return False
  print('True')
  return True

is_prime(4)

