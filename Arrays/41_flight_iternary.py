# This problem was asked by Facebook.

# Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, 
# compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

# For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

# Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

# Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] 
# even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.

def flight_list(flights, start):
  d = {}
  total = len(flights) + 1
  res = []

  for f in flights:
    origin, dest = f

    if origin not in d:
      d[origin] = [dest]
    else:
      d[origin].append(dest)
      d[origin].sort()
  
  while True:
    if d.get(start) and len(d.get(start)) > 0:
      res.append(start)
      start = d[start].pop(0)
    else:
      res.append(start)
      if len(res) == total:
        return res
      else:
        return "NULL"

print(flight_list([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL'))
print(flight_list([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A'))
print(flight_list([('SFO', 'COM'), ('COM', 'YYZ')], 'COM'))
    
    

  