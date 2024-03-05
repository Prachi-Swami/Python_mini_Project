print("### Welcome to the computer QUIZ GAME ###")
play=input("do you want to play game: ").lower()
score=0
if play!="yes":
  quit()
print("ok! Lets Play....")  
answer=input("what does CPU stands for? ")
if answer.lower()=="central processing unit":
  print("Correct!")
  score+=1
else:
  print("Incorrect!")  
answer=input("what does DBMS stands for? ")
if answer.lower()=="database management system":
  print("Correct!")
  score+=1
else:
  print("Incorrect!")  
answer=input("what does SQL stands for? ")
if answer.lower()=="structured query language":
  print("Correct!")
  score+=1
else:
  print("Incorrect!")  
answer=input("what does RDBMS stands for? ")
if answer.lower()=="relational database management system":
  print("Correct!")
  score+=1
else:
  print("Incorrect!")  

print("you got "+str(score)+" "+"questions correct")
print("you got "+str((score/4)*100)+" "+"%.")