def f(x):
    return x**3 + x**2 - 3*x - 3


def main():
    e = 0.0001
    xn = 1
    xn1 = 2
    i = 0
    
    print("|{:^10} | {:^10} |  {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |{:^10}|".format("Iterasi", "Xn", "Xn+1", "Xt","f(Xn)", "f(Xn+1)", "f(Xt)", "f(ft).f(xn)"))
    while abs(f(xn)*f(xn1)) > e:
        i += 1

        xt = xn - f(xn)*(xn1 - xn)/(f(xn1) - f(xn))

        positif_negatif = "+" if f(xt) < 0 else "-"

        print("|{:^10} | {:^10.5f} |  {:^10.5f} | {:^10.5f} | {:^10.5f} | {:^10.5f} | {:^10.5f} | {:^10}|".format(i, xn, xn1, xt, f(xn) , f(xn1) , f(xt) , positif_negatif))
        if f(xn)*f(xt) < 0:
            xn1 = xt
        else:
            xn = xt

if __name__ == "__main__":
    main()

    