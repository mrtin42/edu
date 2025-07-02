lst = ['apple', 'orange', 'pineapple', 'mango', 'kiwi']
target = input('what should we look for').lower()
index = 0
found = False
while found == False and index < len(lst):
  if lst[index] == target:
    found = True
  else:
    index += 1
if found:
  print(f'{target} found at index {index}, position {index+1}')
else:
  print('not found')