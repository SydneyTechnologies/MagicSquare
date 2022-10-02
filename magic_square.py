import math

square = {}


def placeNext(currentPostion, max):
  # placeNext function, determines the next
  # position based on the current position
  x, y = currentPostion
  # created a temporary diagonal position
  diag_x, diag_y = currentPostion
  diag_x += 1
  diag_y += 1
  if diag_x > max and diag_y > max:
    # go down
    x -= 1
  elif diag_x > max:
    # wrap around the columns
    x //= max
    y = diag_y
  elif diag_y > max:
    # wrap around the rows
    y //= max
    x = diag_x
  elif square[(diag_x, diag_y)] != 0:
    # if cell populated go down
    x -= 1
  else:
    x = diag_x
    y = diag_y
  return (x, y)


def Square(max, drawSquare=False):
  for row in reversed(range(1, max + 1)):
    if drawSquare:
      print("\n")
    for column in range(1, max + 1):
      if drawSquare:
        print(square[(row, column)], end="  ")
      else:
        square[(row, column)] = 0


def generateMagicSquare(max):
  # generateMagicSquare function, creates
  # a grid, where max is the length of the grid
  # on both axis
  start = (max, math.ceil(max / 2))

  # populate square with default value 0
  Square(max)

  # populate square accordingly
  for index in range(1, max**2 + 1):
    if index > 1:
      start = placeNext(start, max)
    square[start] = index

  Square(max, drawSquare=True)


generateMagicSquare(3)
