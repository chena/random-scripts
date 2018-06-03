import sys

cases_count = int(raw_input())

def get_row_col(area):
  # TODO
  return None

def read_input():
  input = raw_input()
  sys.stdin.flush()
  return input

def write_output(out):
  print(out)
  sys.stdout.flush()

for x in xrange(cases_count):
  required_area = int(read_input())
  field = set()
  i = 2
  j = 2  
  for _ in xrange(1000):
    write_output('{} {}'.format(i, j))
    prepared_i, prepared_j = read_input().split()
    coordinate = (int(prepared_i), int(prepared_j))
    if coordinate == (0, 0):
      break
    field.add(coordinate)
    if len(field) == 9:
      i += 3
      field = set()