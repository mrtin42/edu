items = ["Florida", "Georgia", "Delaware", "Alabama", "California"]
find = input("which state should be found?")

index = 0
found = False

while found == False and index < len(items):
  if items[index].lower() == find.lower():
    found = True
  else:
    index += 1

if found == True:
  print(f"found at position {index + 1}")
else:
  print("not found")