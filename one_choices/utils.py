rows = 'ABCDEFGHI'
cols = '123456789'


def cross(a, b):
  return [s + t for s in a for t in b]


boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)


def display(values):
  """
  Display the values as a 2-D grid.
  Input: The sudoku in dictionary form
  Output: None
  """
  width = 1 + max(len(values[s]) for s in boxes)
  line = '+'.join(['-' * (width * 3)] * 3)
  for r in rows:
    print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                  for c in cols))
    if r in 'CF': print(line)
  return


def grid_values(grid):
  """
  Convert grid into a dict of {square: char} with '123456789' for empties.
  Input: A grid in string form.
  Output: A grid in dictionary form
          Keys: The boxes, e.g., 'A1'
          Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
  """
  chars = []
  digits = '123456789'
  for c in grid:
    if c in digits:
      chars.append(c)
    if c == '.':
      chars.append(digits)
  assert len(chars) == 81
  return dict(zip(boxes, chars))


def eliminate(values):
  """Eliminate values from peers of each box with a single value.

  Go through all the boxes, and whenever there is a box with a single value,
  eliminate this value from the set of values of all its peers.

  Args:
      values: Sudoku in dictionary form.
  Returns:
      Resulting Sudoku in dictionary form after eliminating values.
  """
  updateList = {}
  defaultValue = '123456789'
  for key in values:
    if values[key] == defaultValue:
      setValues = []
      for peer in peers[key]:
        if len(values[peer]) == 1:
          if not values[peer] in setValues:
            setValues.append(values[peer])
      target = defaultValue
      for idx in setValues:
        target = target.replace(idx, '')
      updateList[key] = target
  values.update(updateList)
  return values
