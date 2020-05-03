cases_count = int(raw_input())
for case in range(cases_count):
  total = 0
  n = int(raw_input())
  matrix = []
  for i in range(n):
    matrix.append([int(x) for x in list(raw_input().split(' '))])
  total = sum([matrix[a][b] for b in range(n) for a in range(n) if a == b])
  r_repeat = len(filter(lambda x: x > 0, [n - len(set(r)) for r in matrix]))
  matrix_rotated = []
  for i in range(n):
    row = [matrix[j][i] for j in range(n)]
    matrix_rotated.append(row)
  c_repeat = len(filter(lambda y: y > 0, [n - len(set(c)) for c in matrix_rotated]))
  print('Case #{}: {} {} {}'.format(case+1, total, r_repeat, c_repeat))