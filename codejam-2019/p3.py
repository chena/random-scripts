cases_count = int(raw_input())

class Location:
  def __init__(self, x, y, d):
    self.x = x
    self.y = y
    self.d = d

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  def __hash__(self):
    return hash(self.x + self.y)

  def distance_to(self, other):
    return sum([abs(self.x - other.x), abs(self.y - other.y)])

  def __str__(self):
    return '({}, {}), {}'.format(self.x, self.y, self.d)

def _move(loc):
    if loc.d is 'N':
      loc.y += 1
    elif loc.d is 'S':
      loc.y -= 1
    elif loc.d is 'E':
      loc.x += 1
    else:
      loc.x -= 1

def _validate_loc(loc, q):
  return loc.x >= 0 and loc.x < q and loc.y >= 0 and loc.y < q

for c in xrange(cases_count):
  rounds = 0
  [p, q] = [int(i) for i in raw_input().split(' ')]
  locations = []
  for pp in xrange(p):
    line = raw_input().split(' ')
    [x, y] = [int(i) for i in line[:2]]
    d = line[2]
    locations.append(Location(x, y, d))
  # for loc in locations:
  #   _move(loc)
  if len(locations) == 1:
    _move(locations[0])
  else:
    while len(set(locations)) > 1 and rounds < 10:
      for loc in locations:
        _move(loc)
        # if not(_validate_loc(loc, q)):
        #   locations.remove(loc)
      rounds += 1
      print([str(l) for l in locations])
      print(rounds)
  for loc in set(locations):
    if _validate_loc(loc, q):
      intersection = loc
      break
  #  print([str(l) for l in locations])
  print('Case #{}: {} {}'.format(c + 1, intersection.x, intersection.y))