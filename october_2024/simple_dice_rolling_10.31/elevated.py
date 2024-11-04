import random


# dice faces
  #check if number
  # check its a valid amount
    # 4, 6, 8, 10, 12, 20
  # if faces already exist yell at user
    # set to var so it skips number of dice interval, this var should reset once it gets to the "do you have another side of dice you want"
# number of dice
  # check its a number



# Do you have another side of dice you want to add to this roll?
  # yes loop
  # no roll

def dice_roll(sides_of_dice):
  print(random.randint(1, sides_of_dice))


face_check = {"4", "6", "8", "10", "12", "20"}
dice_dic= {}
loading_dice = True

while loading_dice:
  while True:
    input_dice_faces =  input("What number of sides of do you want to roll? \n valid inputs are 4, 6, 8, 10, 12, and 20 \n")

    if input_dice_faces.isdigit() and input_dice_faces in face_check:
      input_dice_faces_int = int(input_dice_faces)
      dice_dic[input_dice_faces] = True
      break
    else:
      print("not a valid dice face value, try again you silly goose :)")

  while True:
    input_dice_number = input(f"How many dice would you like to roll with {input_dice_faces} sides?\n")

    if input_dice_number.isdigit():
      dice_dic[input_dice_faces] = int(input_dice_number)
      break
    else:
      print("really, give me that digit!")

  while True:
    input_are_you_ready = input("are you ready to roll your dice? y/n \n ")

    if input_are_you_ready != "y" and input_are_you_ready != "n":
      print("incorrect input try again")
    elif input_are_you_ready == "y":
      loading_dice= False
      break
    else:
      break


for key, x in dice_dic.items():
    print(f'NOW ROLLING {x} SIDED DICE')
    for die in range(x):
        dice_roll(int(key))
