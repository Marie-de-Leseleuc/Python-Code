# lazy solution: https://goo.gl/WE43Bd
# formula used: https://goo.gl/oMNW3S


from math import ceil

# Supported confidence Levels: 50%, 68%, 90%, 95%, and 99% :)
confidence_level_constant = [50,.67], [68,.99], [90,1.64], [95,1.96], [99,2.57]

# Sample size Calculation
def sample_size(population_size, confidence_level, confidence_interval):
  Z = 0.0
  p = 0.5
  e = confidence_interval/100.0
  N = population_size
  n_0 = 0.0
  n = 0.0

  # Loop through supported confidence levels and find the num std
  # deviations for that confidence level
  for i in confidence_level_constant:
    if i[0] == confidence_level:
      Z = i[1]
 
  if Z == 0.0:
    return -1

  # Sample size estimation
  n_0 = ((Z**2) * p * (1-p)) / (e**2)

  # Sample size adjustment for a finite populatio,
  n = n_0 / (1 + ((n_0 - 1) / float(N)) )

  return int(ceil(n))

population_size = 10000
confidence_level = 95.0
confidence_interval = 5.0

sample_size = sample_size(population_size, confidence_level, confidence_interval)

print( "Sample size: {}".format(sample_size))