import random

random_number = random.randint(0,100)
count = 10

while ( x := int(input("Podaj liczbe w zakresie 0-100:"))) != random_number:
    if (x < random_number):
        print("Podałeś zbyt małą liczbę")
    else:
        print("Podałeś zbyt dużą liczbę")
    count = count - 1
    if (count == 0):
        print("Przegrałeś!")
        break
    print(f"Pozostało {count} prób!")
else:
    print("Zgadłeś!")