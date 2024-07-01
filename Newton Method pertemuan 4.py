def f(x):
  return x**3 + x**2 - 3*x - 3
  
def f1(x):
  return 3*x**2 + 2*x - 3 


def main():
  e = 0.000000001
  x1 = 1
  i = 0
  x2 = x1 - f(x1)/f1(x1)
    
  print ("| {:10} | {:10} | {:10} | {:10} | {:10} |".format("Iterasi", "X1", "f(X1)", "X2", "f(X2)"))

  while f(x2) > e:
    i += 1
    print ("| {:10} | {:10.5f} | {:10.5f} | {:10.5f} | {:10.5f} |".format(i, x1, f(x1) , x2, f(x2)))
    x1 = x2
    x2 = x1 - f(x1)/f1(x1)  
if __name__=="__main__":
   main()