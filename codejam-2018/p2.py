"""
Trouble sort = like bubble sort but compare 3 values at a time

Find the index (counting starting from 0) of the first sorting error 
after the algorithm has finished.
"""
cases_count = int(raw_input())

def trouble_sort(values):
  max_iter = len(values) - 2
  for i in xrange(max_iter):
    for i in xrange(max_iter):
      left, right = values[i], values[i + 2]
      if left > right:
        values[i] = right
        values[i + 2] = left

def check_error_index(values):
  error_index = -1
  for i in xrange(len(values) - 1):
    if values[i] > values[i + 1]:
      error_index = i
      break
  return error_index

for i in xrange(cases_count):
  size = int(raw_input())
  values = map(int, raw_input().split(' '))
  trouble_sort(values)
  error_index = check_error_index(values)
  output = 'OK' if error_index < 0 else error_index
  print('Case #{}: {}'.format(i + 1, output))