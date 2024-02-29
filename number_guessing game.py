print("       welcome  User 🎉        ")
import random
top_range= input( "Enter a top_range ⬆ : ")
if top_range.isdigit():
  top_range=int(top_range)
  if top_range<=0:
    print("top_range should be greater than 0")
    quit()
else:
  print("please type number ")
  quit()    
random_number=random.randint(0,top_range)
# print(random_number)
guesses=0
while  True:
  guesses+=1
  user_guess=input("enter your guess: ")
  if user_guess.isdigit():
    user_guess=int(user_guess)
  else:
    print("please enter number")
    continue 
  if user_guess==random_number:
      print("right guess... YOU WON 😎")
      break
  elif user_guess>random_number:
      print("you are above the random number")
  else:
      print(" you are below number")  
print("you got into ",guesses,"guesses")  
