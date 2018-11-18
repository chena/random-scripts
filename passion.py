"""
1. Find the decimal zip of two integers
eg. 12 and 56 -> 1526
eg. 12345 and 678 -> 16273845
"""
def dec_zip(int_a, int_b):
  pos_a = 0
  pos_b = 0
  a = str(int_a)
  b = str(int_b)
  z = ''

  while (pos_a < len(a) and pos_b < len(b)):
    z += a[pos_a] + b [pos_b]
    pos_a += 1
    pos_b += 1

  if pos_a == len(a):
    z += b[pos_b:] if pos_b < len(b) else ''
  elif pos_b == len(b):
    z += a[pos_a:]

  return z


"""
2. Given 4 digits, find the maximum valid time that can be displayed on a digital clock using, if possible
eg. 1, 8, 3, 2 -> 23:18
eg. 3, 0, 7, 0 -> 07:30
eg. 9, 1, 9, 7 -> NOT POSSIBLE
"""
digits = [0] * 10
result = [0] * 4
muri = 'NOT POSSIBLE'

def _find_and_set(pos, index):
  while pos > 0 and digits[pos] == 0:
    pos -= 1
  _set(pos, index)

def _set(value, index=0):
  result[index] = value
  digits[value] -= 1

def max_time(a, b, c, d):
  # count digit occurrence
  for d in [a, b, c, d]:
    digits[d]+=1
  # process hours
  if digits[2] > 0 and sum(digits[:4]) > 1:
    _set(2)
    _find_and_set(3, 1)
  elif digits[1] > 0:
    _set(1)
    _find_and_set(9, 1)
  elif digits[0] > 0:
    _set(0)
    _find_and_set(9, 1)
  else:
    return muri;
  # process minutes
  if sum(digits[:6]) == 0:
    return muri
  _find_and_set(5, 2)
  _find_and_set(9, 3)

  display = [str(r) for r in result]
  return ''.join(display[:2]) + ':' + ''.join(display[2:])


# print dec_zip(12345, 678)
print(max_time(9, 1, 9, 7))