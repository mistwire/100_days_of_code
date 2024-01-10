# How to modify a global variable inside a function:


enemies = 1

def increase_enemies():
  # the global keyword pulls the global variable into the function
  # this is something you don't want to do often 
  global enemies
  enemies += 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# instead what you should do is use return to modify the amount:

enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

