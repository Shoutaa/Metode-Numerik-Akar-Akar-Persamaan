def f(x):
    return x**3 + x**2 + 3*x - 3

def main():
    e = 0.0001
    xn = 1
    xn1 = 2
    i = 0

    print("|{:^10} | {:^10} |  {:^10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10}|".format("Iterasi", "Xn", "Xn+1", "Xt","f(Xn)", "f(Xn+1)", "f(Xt)", "f(ft).f(xn)"))

    while abs(xn - xn1) > e:
        i += 1
        xt = (xn + xn1) / 2
        f_xn = f(xn)
        f_xn1 = f(xn1)
        f_xt = f(xt)

        f_xn_sign = "+" if f_xn > 0 else "-"
        f_xn1_sign = "+" if f_xn1 > 0 else "-"
        f_xt_sign = "+" if f_xt > 0 else "-"

        print("|{:^10} |  {:^10.5f} | {:^10.5f} | {:^10.5f} | {:^10.5f} | {:^10.5f} | {:^10.5f} | {:^10} |".format(i, xn, xn1, xt, f_xn, f_xn1, f_xt, f_xt_sign))

        if f_xt * f_xn < 0:
            xn1 = xt
        else:
            xn = xt


if __name__ == "__main__":
    main()
