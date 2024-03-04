print("....welcome user....")
with open("story.txt","r") as f:
 story= f.read()
# print(story) 
angle_words=set()
start_of_Word=-1
start_target="<"
end_target=">"
for index,item in enumerate(story):
  if item==start_target:
    start_of_Word=index
  if item==end_target and start_of_Word!=-1:
    word=story[start_of_Word:index+1]
    angle_words.add(word)
    start_of_Word=-1
answers={} 
for word in angle_words:
  answer=input("enter a word for "+word+ ":")  
  answers[word] = answer
for word in angle_words:
  story=story.replace(word,answers[word])  
print(story)  



 


 