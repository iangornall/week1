def create_histogram(items):
  histogram = {}
  for item in items:
    if item not in histogram:
      histogram[item] = 1
    else:
      histogram[item] += 1
  return histogram