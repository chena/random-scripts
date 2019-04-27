cases_count = int(raw_input())

for c in xrange(cases_count):
	n = int(raw_input())
	lydia = list(raw_input())
	steps = len(lydia)
	lydia_path = [(0, 0)]
	x = 0
	y = 0
	for i in xrange(steps):
		if lydia[i] == 'E':
			x += 1
		else:
			y += 1
		lydia_path.append((x, y))

	x = 0
	y = 0
	path = [(0, 0)]
	ans = []
	backtrack = False
	for i in xrange(steps):
		if (path[i] == lydia_path[i]):
			if (lydia[i] == 'E'):
				y += 1
				ans.append('S')
			else:
				x += 1
				ans.append('E')
		else:
			if (x == y):
				if (lydia[i] == 'E'):
					x += 1
					ans.append('E')
				else:
					y += 1
					ans.append('S')
			elif x <= y:
				x += 1
				ans.append('E')
			else:
				y += 1
				ans.append('S')
		path.append((x, y))
	print('Case #{}: {}'.format(c + 1, ''.join(ans)))