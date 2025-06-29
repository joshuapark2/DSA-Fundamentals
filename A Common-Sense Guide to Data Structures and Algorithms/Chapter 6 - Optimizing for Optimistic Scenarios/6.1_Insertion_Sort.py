'''
array = [4, 2, 7, 1, 3]

1. Iterate through the range of algorithm starting at index 1
2. Start by storing the variable we want to sort and a position variable to compare previous elements
3. Create passes 1 through n with a while loop that stops when we reach the front.
4. Compare if the position element we’re checking is greater than the element we want to swap
5. Swap if the condition passes → But swap only one to the right, otherwise this would be selection sort.
6. Decrement Position and Repeat
7. Break to go onto the next pass-through otherwise
8. Once we exit the while loop, wherever the lowest position we ended up, increment position by 1 and place
  temp value there.

'''

'''
  [4, 2, 7, 1, 3]
   0, 1, 2, 3, 4 = index ||| len(array) = 5
'''

def insertion_sort(array):
  for index in range(1, len(array)):
    temp_value = array[index]
    position = index - 1

    while position >= 0:
      if array[position] > temp_value:
        array[position + 1] = array[position]
        position -= 1
      else:
        break
      
    array[position + 1] = temp_value

  return array