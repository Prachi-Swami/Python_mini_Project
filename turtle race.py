import turtle
import random
WIDTH,HEIGHT=500,500
COLORS=["Red","Blue","Green","Orange","Black","Pink","Cyan","Yellow","Purple","Brown"]

def get_number_of_turtle():
  racers=0
  while True:
    racers=input("Enter the number of racers you want (2 - 10)  ")
    if racers.isdigit():
      racers=int(racers)
    else:
      print("Enter a digit number value only.....TRY AGAIN.... ")
      continue
    if 2<=racers<=10:
      return racers
    else:
      print("number not in range 2 -   10")
def race(colors):
  turtles=create_turtles(colors)
  while True:
    for racer in turtles:
      distance=random.randrange(1,20)
      racer.forward(distance)
      x,y=racer.pos()
      if y>=HEIGHT//2-10:
        return colors[turtles.index(racer)]

def create_turtles(colors):
  turtles=[]
  spacing_x=WIDTH//(len(colors)+1)#len(color)=number of turtles
  for i,color in enumerate(colors):
    racer=turtle.Turtle()
    racer.color(color)
    racer.shape("turtle")
    racer.pendown()
    racer.left(90)
    racer.penup()
    racer.setpos(-WIDTH//2+(i+1)*spacing_x,-HEIGHT//2+20)
    turtles.append(racer)
  return turtles  

def init_turtle():
  screen= turtle.Screen()
  screen.setup(WIDTH,HEIGHT)
  screen.title("Turtle Racing.....") 

racers=get_number_of_turtle()
# print(racers)
init_turtle()
random.shuffle(COLORS)
colors=COLORS[:racers]
winner=race(colors)
print(winner)



