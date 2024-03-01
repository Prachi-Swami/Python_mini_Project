print("    welcome to the adventure    ")
name=input("type your name: ")
print("welcome", name, "to the game!")
answer=input("You are on a road and you can go left or right. which way would you choose Left or Right? ").lower()
if answer=="left":
  answer=input("you came to river,you can walk around it or swim across? type walk to walk and swim to swim ").lower()
  if answer=="swim":
    print("you came across and were eaten by alligator")
  elif answer=="walk":
    print("you walked for many miles,ran out of water and you lost the game. ☹ ")
  else:
    print("not a valid option.you loose")
elif answer=="right":
  answer=input("you came to bridge,do you want to go back or cross the bridge? ")
  answer=answer.lower()
  if answer=="back":
    print("you go back and loose.")
  elif answer=="cross":
    answer=input("you cross the bridge and met stranger do you talk to them (yes/no)?" )
    answer=answer.lower()
    if answer=="yes":
      print("You talk to the stranger and they give you gold,you won!!!🏆")
    elif answer=="no":
      print("You ignore the stranger and they are offended and you lose....☹")  
    else:
      print("Not a valid option you loose")
else:
  print("Not a valid option you loose")





