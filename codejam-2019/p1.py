cases_count = int(raw_input())

for c in xrange(cases_count):
	n = int(raw_input())
	n1 = 1
	n2 = [int(v) for v in list(str(n - 1))]

	for i in xrange(len(n2)):
		pos = -(i + 1)
		v = n2[pos]
		if v == 4:
			n1 += 10 ** i
			n2[pos] -= 1
	print('Case #{}: {} {}'.format(c + 1, n1, ''.join([str(d) for d in n2])))