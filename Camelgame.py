import random

health_count = [100]
distance_count = [0]
camel_count = [100]
thirst_count = [100]
canteen_count = [3]
you_dead_list = [0]
natives = -20

# Main information on screen


def start():
    print("*************************************************************************")
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down!")
    print("Survive your desert trek and outrun the natives.")
    print("*************************************************************************")


def interface():
    print("*************************************************************************")
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop and rest.")
    print("E. Status check.")
    print("Q. Quit. ")
    choice = input("Input: ")
    print("*************************************************************************")
    return choice


def status(dist, cam, heal, thir, cant):
    print("*************************************************************************")
    print("Distance", dist, "   Camel", cam)
    print("Health", heal)
    print("Thirst", thir, "     Canteen", cant)
    print("*************************************************************************")

# Status Effects


def health(x):
    z = health_count[0]
    an = z - x
    health_count.clear()
    health_count.append(an)
    if an < 0:
        print("You are to injured to get back on the camel, the natives have captured you and the camel")
        you_dead_list.clear()
        you_dead_list.append(1)
    return an


def distance(x):
    return x


def camel(x):
    return x


def thirst(x, y):
    z = thirst_count[0]
    an = z + x - y
    thirst_count.clear()
    thirst_count.append(an)
    if an < 0:
        print("You passed out from dehydration and died")
        you_dead_list.clear()
        you_dead_list.append(1)
    return an


def canteen(x):
    z = canteen_count[0]
    x = z - x
    canteen_count.clear()
    canteen_count.append(x)
    return x


def luck():
    count = random.randrange(1, 10)
    return count


def luck_consequence():
    x = random.randrange(1, 10)
    if x == 1:
        print("You fall off the camel and are injured you only traveled half the distance you could of today")
        health(50)
        return
    elif x == 2:
        print("You drop your canteen spilling anything left.")
        canteen_count.clear()
        canteen_count.append(0)
        return
    elif x == 3:
        print("None")
    elif x == 4:
        print("None")
    elif x >= 5:
        print("You luck is holding up")


def decision(x):
    if x == "a" or "b" or "c" or "d" or "e":
        return False
    elif x == "q":
        return True


def you_dead(x):
    if x == 0:
        return False
    elif x == 1:
        return True


def main(x):
    start()
    done = False
    while done is False:
        user_in = interface()
        done = decision(user_in)
        if user_in == "a":
            drink = canteen(1)
            if drink < 0:
                print("Canteen is empty")
                canteen_count.clear()
                canteen_count.append(0)
            elif drink >= 0:
                thirst(25, 0)
                print("You drunk from your canteen, you have", drink, "drinks left")
        elif user_in == "b":
            x = x + random.randrange(0, 10)
            by = random.randrange(3, 8) + distance_count[0]
            bz = luck()
            if bz == 1:
                luck_consequence(bz)
                by /= 2
            else:
                luck_consequence(bz)
            b_total = x - by
            b_total = b_total * -1
            print("The native are", b_total, "km behind you.")
            distance_count.clear()
            distance_count.append(by)
            thirst(0, 10)
        elif user_in == "c":
            x = x + random.randrange(0, 10)
            cy = random.randrange(3, 8) + distance_count[0]
            cz = luck()
            if cz == 1:
                luck_consequence(cz)
                cy /= 2
            else:
                luck_consequence(cz)
            c_total = x - cy
            distance_count.clear()
            distance_count.append(c_total)
            thirst(0, 15)
        elif user_in == "d":
            x = x + 7 + random.randrange(0, 7)
            print("natives are", x, "km away")
            thirst(0, 20)
        elif user_in == "e":
            status(distance_count[0], camel_count[0], health_count[0], thirst_count[0], canteen_count[0])
        if done is False:
            done = you_dead(you_dead_list[0])


main(natives)
