from random import randint


def ran():
    a = int(input("start"))
    b = int(input("stop"))
    return b, a


def randik(ran):
    (b, a) = ran()
    if 30 >= b - a and b - a >= 4:
        first = int(randint(a, b))
        second = int(randint(a, b))
        third = int(randint(a, b))
        c = (first, second, third)
        print(c)
    else:
        quit()

    def your_choice():
        while True:
            a1 = input("your first number")
            if "exit" in a1:
                quit()
            b1 = input("your second number")
            if 'exit' in b1:
                quit()
            c1 = input("your second number")
            if 'exit' in c1:
                quit()
            if int(a1) == first and second == int(b1) and third == int(c1):
                print("You win!")
                break
            else:
                print('Try again!')
            list1 = [a1, b1, c1]
            list2 = [first, second, third]
            match = 0
            for x in list1:
                if int(x) in list2:
                    match = match + 1
            print(f'Matched numbers={match}')

    print(your_choice())


randik(ran)
