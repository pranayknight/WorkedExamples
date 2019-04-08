films = {
    "Finding Dory":[3,5],
    "Singham":[18,5],
    "Yevadu":[15,5],
    "Ghost Busters":[12,5]
    }

while True:
    choice = input("What film would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())

        # chech user age
        if age>=films[choice][0]:

            if films[choice][1]>0:
                print("Enjoy the film...")
                films[choice][1] = films[choice][1]-1
            else:
                print("Sorry, we are sold out!")
                
        else:
            print("You too young to see that film")
            
    else:
        print("We don't have that film...")
