try:
    from colorama import init


    init()


    from colorama import Fore

    from math import factorial as f

    from math import sqrt as sq

    from math import isqrt



    def mnozenie(a, b):
        return a * b


    def dzielenie(a, b):
        return a / b


    def dzielenie_(a, b):
        return a % b


    def dodawanie(a, b):
        return a + b


    def odejmowanie(a, b):
        return a - b


    def potęgowanie(a, b):
        return a ** b


    def bmi(waga, wzrost):
        return waga / (wzrost / 100) ** 2


    def przelicznik_predkosci(tryb, predkosc):
        if tryb == 0:
            return predkosc * 3.6
        if tryb == 1:
            return predkosc / 3.6



    powiadomienie_ = "ValueError,mozliwe powody: w przypadku silni podana liczba minusowa lub podana wartosc nie jest liczba lub jest liczba zmiennoprzecinkowa, lub wykladnik potegi jest inny niż integer."

    print(Fore.MAGENTA + "")

    werjsa = "1.4"

    print("kalkulatorr " + werjsa)

    print(Fore.GREEN + "")

    print("CO NOWEGO:\n")

    print(Fore.YELLOW + "")

    print(
        "Dodano przelicznik predkosci.\n\n\nTIP:W liczbch float musisz napisac kropke zamiast przecinku "
        "np.3.14 - poprawnie, 3,14 -zle(jest tak ponieważ nie chciało mi sie napisać replace'a)")

    print("\n")

    while True:
        try:
            print(Fore.RED + "")
            try:
                wybór = int(input(
                    "Wybierz dzialanie? wpisz liczbę od 1 do 9 \n1.mnozenie\n2.dzielenie\n3.dodawanie\n4.odejmowanie\n5.potegowanie\n6.silnie\n7.pierwiastek kwadratowy\n8.BMI\n9.przelicznik predkosci: "))
                if wybór < 1 or wybór > 9:
                    print(Fore.LIGHTWHITE_EX + "")
                    print("Wartosc musi być integer'em od 1 do 9.")
                if wybór == 1:
                    print(Fore.WHITE + "")
                    c = float(input("podaj czynnik: "))
                    d = float(input("podaj czynnik: "))
                    wynik = round(mnozenie(c, d), 6)
                    wynik_ = Fore.CYAN + str(wynik)

                    print(wynik_)
                if wybór == 2:
                    print(Fore.WHITE + "")
                    c = float(input("podaj dzielna:  "))
                    d = float(input("podaj dzielnik: "))
                    if c and d != 0:
                        if dzielenie_(c, d) == 0:
                            wynik = round(dzielenie(c, d))
                            wynik_ = Fore.CYAN + str(wynik)

                            print(wynik_)

                        else:
                            wynik = dzielenie(c, d)
                            wynik_ = Fore.CYAN + str(wynik)

                            print(wynik_)

                    else:
                        print(Fore.YELLOW + "")
                        print("Nie mozna dzielic przez zero.")

                if wybór == 3:
                    print(Fore.WHITE + "")
                    c = float(input("podaj składnik: "))
                    d = float(input("podaj składnik: "))
                    wynik = round(dodawanie(c, d), 6)
                    wynik_ = Fore.CYAN + str(wynik)

                    print(wynik_)
                if wybór == 4:
                    print(Fore.WHITE + "")
                    c = float(input("podaj odjemna:  "))
                    d = float(input("podaj odjemnik: "))
                    wynik = round(odejmowanie(c, d), 6)
                    wynik_ = Fore.CYAN + str(wynik)

                    print(wynik_)
                if wybór == 5:
                    print(Fore.WHITE + "")
                    c = float(input("podaj podstawe potegi:  "))
                    d = int(input("podaj wykładnik potegi: "))
                    wynik = round(potęgowanie(c, d), 6)
                    wynik_ = Fore.CYAN + str(wynik)

                    print(wynik_)
                if wybór == 6:
                    print(Fore.WHITE + "")
                    c = int(input("podaj liczbe z której chcesz uzyskac silnię: "))
                    wynik = f(c)
                    wynik_ = Fore.CYAN + str(wynik)

                    print(wynik_)
                if wybór == 7:
                    print(Fore.WHITE + "")
                    c = float(input("podaj liczbe z ktorej chcesz uzyskac pierwiastek kwadratowy: "))
                    wynik = sq(c)
                    wynik_ = Fore.CYAN + str(wynik)

                    print(wynik_)
                if wybór == 8:
                    print(Fore.WHITE + "")
                    c = int(input("podaj swoja wagę(kg): "))
                    d = int(input("podaj swoj wzrost(cm): "))
                    wynik = round(bmi(c, d), 6)
                    wynik_ = Fore.CYAN + str(wynik)

                    print(wynik_)
                if wybór == 9:
                    c = None
                    d = None
                    print(Fore.WHITE + "")
                    while c != 1 and c != 2:
                        c = int(input("podaj tryb przeliczania(1.m/s na km/h, 2.km/h na m/s: "))
                    if c == 1:
                        c = 0
                    else:
                        c = 1
                    d = int(input("podaj prędkość: "))
                    wynik = round(przelicznik_predkosci(c, d), 6)
                    wynik_ = Fore.CYAN + str(wynik)


                    print(wynik_)




            except ValueError:
                print(
                    "ValueError,mozliwe powody: w przypadku silni podana liczba minusowa lub podana wartosc nie jest liczba lub jest liczbą zmiennoprzecinkowa, lub wykladnik potegi jest inny niz integer.")

        except KeyboardInterrupt:
            print("KeyboardInterrupt(Error) został obsłużony.")




except KeyboardInterrupt:
    print("KeyboardInterrupt(Error) został obsłużony")