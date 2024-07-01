def f(x):
  return x**3 + x**2 - 3*x - 3

def g(x):
  return (-x**2 + 3*x + 3)**(1/3)

def error(x1, x2):
  return abs((x2-x1)/x2) * 100

def main():
  epsilon = 0.00001
  x1 = 1
  x2 = g(x1)
  i = 0
  print("|{:^10} | {:^10} | {:^10} | {:^10} | {:^10}|".format("Iterasi", "X1", "X2", "Ea (%)", "e"))
  while error(x1, x2) > epsilon:
    i += 1
    print("|{:^10} | {:^10.5f} | {:^10.5f} | {:^10.5f} | {:^10.5f}|".format(i, x1, x2, error(x1, x2), epsilon))
    x1 = x2
    x2 = g(x1)

if __name__ == "__main__":
  main()
