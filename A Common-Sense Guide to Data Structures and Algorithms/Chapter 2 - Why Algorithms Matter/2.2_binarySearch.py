

def binary_search(array, search_value):
  '''
  First, we establish the lower and upper bounds of where the value
  we're search for can be. To start, the lower bound is the first value
  in the array, while the upper bound is the last value.
  '''
  lower_bound = 0
  upper_bound = len(array) - 1
  steps = 0

  '''
  We begin a loop in which we keep inspecting the middlemost value
  between the upper and lower bounds.
  '''
  while lower_bound <= upper_bound:
    '''
    We find the mindpoint between the upper and lower bounds:
      Using Python Floor division '//' to always round down
    '''
    midpoint = (upper_bound + lower_bound) // 2
    # Inspect value at midpoint
    value_at_midpoint = array[midpoint]

    '''
    If the value at the midpoint is the one we're looking for, we're done
    If not, we change the lwoer or upper bound based on whether we need
    to guess higher or lower:
    '''
    if search_value == value_at_midpoint:
        print(midpoint, steps)
        return midpoint
    elif search_value < value_at_midpoint:
        upper_bound = midpoint - 1
        
    elif search_value > value_at_midpoint:
        lower_bound = midpoint + 1
    steps += 1
  print('None', steps)
  return None


binary_search([2, 4, 6, 8, 10, 12, 13], 7)
# Worst case for [2, 4, 6, 8, 10, 12, 13] = 3