# Very simple, given an integer or a floating-point number, find its opposite.

# Examples:

# 1: -1
# 14: -14
# -34: 34

def opposite(number):
  return abs(number) if number < 0 else (0 - number)