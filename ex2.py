# Write a function that prints all factors of the given parameter x
def print_factor(x):
  r = []
  for i in range(1, x+1):
    if x%(i) == 0:
      r.append(i)
  print(r)

if __name__ == '__main__':
    print_factor(52633)