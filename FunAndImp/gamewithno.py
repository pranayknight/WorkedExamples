# Health game
import random

health = 50

difficulty = int(input("Enter any number from 1 to 3 to set the level of difficulty: "))

potion_health = int(random.randint(25, 50) / difficulty)

health = health = health + potion_health

print(health)
