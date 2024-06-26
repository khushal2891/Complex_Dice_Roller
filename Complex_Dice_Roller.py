import random

#remember this codes ! to make your dice more attractive

 #  ● ┌ ─ ┐ └ ┘

"┌─────────┐"
"|         |"
"|         |"
"|         |"
"└─────────┘"

#Create dictionary
#Make all boxes

Dice_art = {
    1:("┌─────────┐",
       "|         |",
       "|    ●    |",
       "|         |",
       "└─────────┘"),
    2:("┌─────────┐",
       "| ●       |",
       "|         |",
       "|       ● |",
       "└─────────┘"),
    3:("┌─────────┐",
       "| ●       |",
       "|    ●    |",
       "|       ● |",
       "└─────────┘"),
    4:("┌─────────┐",
       "| ●     ● |",
       "|         |",
       "| ●     ● |",
       "└─────────┘"),
    5:("┌─────────┐",
       "| ●     ● |",
       "|    ●    |",
       "| ●     ● |",
       "└─────────┘"),
    6:("┌─────────┐",
       "| ●     ● |",
       "| ●     ● |",
       "| ●     ● |",
       "└─────────┘")
}

#Create a list of numbers 

dice=[]
total =0
number_of_dice = int(input("How many dices ? : \n "))
for die in range(number_of_dice):
 dice.append(random.randint(1,6))

print(dice)

for die in range(number_of_dice):
   for line in Dice_art.get(dice[die]):
      print(line)

for die in dice:
    total+=die
print(f"total: {total}")

#In python we have to give proper space between code functions 

#ProjectiFire ! 
#Khushal !