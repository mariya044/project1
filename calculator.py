def calculator():
    print("Для выхода введите q в качетсве знака операции ")
    while True:
        s = input("Знак(+,-,*,/,**)")
        if s == "q":
            quit()
        return s


def variables():
    while True:
        try:
            x = int(input("x="))
            y = int(input("y="))
        except ValueError:
            print('Error')
            quit()
        else:
            ...
            return x, y


def sign(calculator, variables):
    while True:
        sign = calculator()
        (x, y) = variables()
        if sign in ("+", "-", "*", "/", "**"):
            if sign == "+":
                print(x + y)
            elif sign == "**":
                print(x ** y)
            elif sign == "-":
                print(x - y)
            elif sign == "*":
                print(x * y)
            elif sign == "/":
                try:
                    print(int(x / y))
                except ZeroDivisionError as err:
                    print(f"y is zero-{err}!")


sign(calculator, variables)
