# Find the all factors of x using a loop and the operator % 
# % means find remainder, for example 10 % 2 = 0; 10% 3 = 1
x = 52633
r = []
for i in range(1, x+1):
  if x%(i) == 0:
    r.append(i)
print(r)