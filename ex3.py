# Write a program that be able to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]

def print_factor(input):
  r = []
  for j in range(len(input)):
    x = input[j]
    print(x)
    for i in range(1, x+1):
      if x%(i) == 0:
        r.append(i)
    print(r)
    r=[]
    
if __name__ == '__main__':
  print_factor(l)