import random
import time
name=input("Enter user name: ")
COUNT_OF_PROBLEM=int(input("How many number of problems you  want to solve:  "))
operators=["+","*","-"]
right_side_operand=random.randint(2,20)
left_side_operand=random.randint(2,20)
def create_math_problem():
  operator=random.choice(operators)
  expression=str(left_side_operand)+" "+operator+" "+str(right_side_operand)
  evaluate=eval(expression)
  return  expression,evaluate
create_math_problem()
wrong=0
input("press enter to start")
print("_____#######_____")
start_time=time.time()
for i in range(COUNT_OF_PROBLEM):
  expression,evaluate=create_math_problem()
  while True:
      user_Answer=input("problem"+" "+str(i+1)+ ":"+" "+expression + "=" )
      if user_Answer==str(evaluate):
        print(" Correct....✔")
        break
      wrong+=1 
end_time=time.time() 
total_time=round(end_time-start_time,2) 
print("You finished in",total_time, "seconds")
print("------------------") 
print("Good JOB",name)