def decision():
    print("Player 2 is computer.")
    desc = input("Do you want to start the game? ")
    if desc == "yes":
        yes()
        print("\n\nCONGRATULATIONS!!!")
        print("YOU WON!")
        exit(0)
    else:
        print("Ok")
        exit(0)


def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near


def check(lst):
    i = 1
    while i < len(lst):
        if (lst[i] - lst[i - 1]) != 1:
            return False
        i += 1
    return True


def lose():
    print("You lost!")
    exit(0)


def yes():
    lst = []
    last = 0
    print("Enter 'F' to take the first chance.\nEnter 'S' to take the second chance.")
    enter = input()
    if enter == "F":
        First(lst, last)
    elif enter == "S":
        Second(lst, last)
    else:
        print("Wrong choice")


def First(lst, last):
    while True:
        if last == 20:
            lose()
        else:
            print("\nYour Turn.")
            print("\nHow many numbers do you wish to enter?")
            inp = int(input())

            if inp > 0 and inp <= 3:
                comp = 4 - inp
            else:
                print("Wrong input. You are disqualified from the game.")
                lose()

            i, j = 1, 1

            print("Now enter the values")
            while i <= inp:
                a = int(input())
                lst.append(a)
                i += 1

            last = lst[-1]
            if check(lst) is True:
                if last == 21:
                    lose()
                else:
                    while j <= comp:
                        lst.append(last + j)
                        j += 1
                    print("Order of inputs after the computer's turn is: ")
                    print(lst)
                    last = lst[-1]
            else:
                print("\nYou did not input consecutive integers.")
                lose()


def Second(lst, last):
    comp = 1
    while last < 20:
        j = 1
        while j <= comp:
            lst.append(last + j)
            j += 1
        print("Order of inputs after the computer's turn is:")
        print(lst)
        if lst[-1] == 20:
            lose()
        else:
            print("\nYour turn.")
            print("\nHow many numbers do you wish to enter?")
            inp = int(input())
            i = 1
            print("Enter your values")
            while i <= inp:
                lst.append(int(input()))
                i = i + 1
            last = lst[-1]
            if check(lst) is True:
                near = nearestMultiple(last)
                comp = near - last
                if comp == 4:
                    comp = 3
                else:
                    comp = comp
            else:
                print("\nYou did not input consecutive integers.")
                lose()


decision()
