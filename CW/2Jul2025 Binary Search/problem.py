items = ["florida", "georgia", "delaware", "alabama", "california"]

n = len(items)
swapped = True

while n > 0 and swapped == True:
  swapped = False
  n = n - 1
  for i in range(0,n):
    if items[i] > items[i+1]:
      temp = items[i]
      items[i] = items[i+1]
      items[i+1] = temp
      swapped = True
    
  print(items)