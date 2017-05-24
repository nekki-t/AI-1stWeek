from utils import *


def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    # TODO: Implement only choice strategy here
    for unit in unitlist:
        for box in unit:
            nums = list(values[box])

            otherValues = []
            for key in unit:
                if key != box:
                    otherValues += list(values[key])
            otherValues = list(set(otherValues))
            otherValues.sort()

            for num in nums:
                if num not in otherValues:
                    values[box] = num
    return values



values = {'F9': '345', 'F7': '2', 'C1': '25', 'G5': '478', 'C8': '23579', 'I1': '46', 'H7': '17', 'B3': '47',
          'C5': '79', 'E2': '123459', 'A3': '3', 'B9': '1', 'G7': '5', 'A4': '49', 'A5': '2', 'H8': '1467', 'A6': '147',
          'C6': '6', 'E6': '4', 'B6': '5', 'E7': '1', 'I2': '4679', 'B4': '3', 'I4': '4', 'A9': '57', 'F2': '13459',
          'A7': '6', 'E9': '8', 'I5': '1', 'F1': '1345', 'C4': '8', 'D8': '34567', 'D6': '2', 'A1': '45', 'E5': '34569',
          'D7': '9', 'B7': '78', 'G4': '6', 'H4': '2', 'F6': '8', 'B8': '278', 'E4': '459', 'I8': '24678', 'I9': '2467',
          'C9': '2357', 'H2': '1467', 'I3': '5', 'H1': '8', 'D5': '3456', 'B5': '47', 'D9': '34567', 'A8': '5789',
          'G6': '9', 'G8': '1478', 'C7': '4', 'G1': '134', 'H3': '47', 'G3': '2', 'E3': '49', 'I7': '3', 'F5': '3459',
          'D1': '345', 'H9': '9', 'G2': '1347', 'D3': '8', 'B1': '9', 'E1': '7', 'F4': '7', 'I6': '47', 'H5': '457',
          'F8': '1345', 'E8': '13456', 'G9': '47', 'D2': '345', 'F3': '6', 'B2': '24678', 'D4': '1', 'C3': '1',
          'A2': '4578', 'C2': '257', 'H6': '3'}
print(only_choice(values))
