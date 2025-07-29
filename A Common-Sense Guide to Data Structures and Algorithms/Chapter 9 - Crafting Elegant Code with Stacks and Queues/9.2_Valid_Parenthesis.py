def is_valid(s: str) -> bool:
  stack = []
  validPairs = { '(': ')', '{': '}', '[': ']'}

  if len(s) <= 1:
      return False

  for letter in s:
      if letter in validPairs:
          stack.append(letter)
      elif len(stack) > 0 and letter == validPairs[stack[-1]]:
          stack.pop()
      else:
          return False

  if len(stack) != 0:
      return False
  else:
      return True
  
'''
Edge Cases:
')(){}' and '){'
'()' - index out of bounds -> Order matters and putting len(stack) > 0 first fixes this
'''

# NeetCode Solution Below:
def neet_is_valid(s: str) -> bool:  
  stack = []
  validPairs = { ')': '(', '}': '{', ']': '['}

  for letter in s:
      if letter in validPairs:
          if stack and stack[-1] == validPairs[letter]:
              stack.pop()
          else:
              return False
      else:
          stack.append(letter)
  return True if not stack else False