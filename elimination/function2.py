from utils import *

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    assert len(grid) == 81
    newgrid = []
    for s in grid:
      if s == '.':
        newgrid.append('123456789')
      else:
        newgrid.append(s)
    return dict(zip(boxes, newgrid))

list = grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
display(list)

def eliminate(values):
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
  # solved_values = [box for box in values.keys() if len(values[box]) == 1]
  # for box in solved_values:
  #   digit = values[box]
  #   for peer in peers[box]:
  #     values[peer] = values[peer].replace(digit, '')
  # return values
display(eliminate(list))

