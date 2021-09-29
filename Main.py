import random
ver = 0
while (ver == 0):
    a = random.randint(1,100)
    ver = 1
    while (ver == 1):
        b = int(input("Number?\n"))
        if (b > a):
            print("Maybe less")
        if (b < a):
            print("Maybe more")
        if (b == a):
            print("Wow you guessed it!")
    
