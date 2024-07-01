def f(x):
    return x**3 + x**2 - 3*x - 3

def menghitung_x2(x0, x1):
    return x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))  

def main():
    e = 0.00001
    x0 = 1
    x1 = 2

    i = 0
    print("|{:^10} | {:^10} | {:^10} | {:^10}| {:^10} | {:^10} | {:^10} |".format("Iterasi", "X0", "X1", "f(x0)", "f(x1)", "x2", "f(x2)"))   
    while abs(f(menghitung_x2(x0, x1))) > e:
        i += 1
        x2 = menghitung_x2(x0, x1)
        print("|{:^10} | {:^10.5f} | {:^10.5f} | {:^10.5f}| {:^10.5f} | {:^10.5f} | {:^10.5f} |".format(i, x0, x1, f(x0), f(x1), x2, f(x2)))   
        x0 = x1
        x1 = x2


if __name__ == "__main__":
    main()    