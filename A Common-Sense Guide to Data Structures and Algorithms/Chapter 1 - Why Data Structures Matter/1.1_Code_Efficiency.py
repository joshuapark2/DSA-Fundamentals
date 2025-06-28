# V1 looping 100 steps vs. V2 looping 50 steps

def print_numbers_version_one():
  number = 2

  while number <= 100:
    if number % 2 == 0:
      print(number)
    number += 1
  

def print_number_version_two():
  number = 2

  while number <= 100:
    print(number)
  
  number += 2