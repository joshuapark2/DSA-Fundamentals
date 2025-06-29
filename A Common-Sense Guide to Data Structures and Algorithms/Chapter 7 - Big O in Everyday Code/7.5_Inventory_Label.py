'''
Fifth Algorithm: Takes in an array of strings of clothing items and we want to create labels 
  where each item has a size that ranges from 1 to 5.

Array Input: ["Purple Shirt", "Green Shirt"]

Array Result:
  [
  "Purple Shirt Size: 1",
  "Purple Shirt Size: 2",
  "Purple Shirt Size: 3",
  "Purple Shirt Size: 4",
  "Purple Shirt Size: 5",
  "Green Shirt Size: 1",
  "Green Shirt Size: 2",
  "Green Shirt Size: 3",
  "Green Shirt Size: 4",
  "Green Shirt Size: 5"
  ]
'''


def mark_inventory(clothing_items): 
  clothing_options = []
  for item in clothing_items:
    # For sizes 1 through 5 (Python ranges go UP TO second 
    # # number, but do not include it):
    for size in range(1, 6):
      clothing_options.append(item + " Size: " + str(size)) 
  return clothing_options