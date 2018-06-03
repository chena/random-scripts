"""
What is this smallest possible number of swaps 
which will ensure that the program does no more than D total damage,

# C = change = double
# S - shoot = increment damage count
"""
cases_count = int(raw_input())

def swap(instructions):
  # swap S to the front
  ind = 0
  swap_done = False
  while not swap_done and ind < len(instructions) - 1:
    left, right = instructions[ind], instructions[ind + 1]
    if left == 'C' and right == 'S':
      instructions[ind] = right
      instructions[ind + 1] = left
      swap_done = True
    ind += 1
  return swap_done

def get_total(instructions):
  curr_value = 1
  total = 0
  for i in instructions:
    if i == 'S':
      total += curr_value
    else:
      curr_value *= 2
  return total

for i in xrange(cases_count):
  line = raw_input().strip().split(' ')
  max_total = int(line[0])
  instructions = list(line[1])
  swaps = 0
  total = get_total(instructions)
  impossible = False
  while total > max_total:
    swapped = swap(instructions)
    if not swapped:
      impossible = True
      break
    swaps += 1
    total = get_total(instructions)
  print('Case #{}: {}'.format(i + 1, 'IMPOSSIBLE' if impossible else swaps))

