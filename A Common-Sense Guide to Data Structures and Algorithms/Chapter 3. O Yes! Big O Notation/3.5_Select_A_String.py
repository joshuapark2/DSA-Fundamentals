def selectAString(array):
  newArray = []

  for string in array:
    if string.startswith("a") or string.startswith("A"):
      newArray.append(string)
  print(newArray)
  return newArray

selectAString('SuperAllStar')