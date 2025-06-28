def chessboardSpace(numberOfGrains):
  chessBoardSpaces = 1
  placedGrains = 1

  while placedGrains < numberOfGrains:
    placedGrains *= 2 # Increase Exponentially O(n)
    chessBoardSpaces += 1 # increases Logarithmically O(log n)
  
  return chessBoardSpaces