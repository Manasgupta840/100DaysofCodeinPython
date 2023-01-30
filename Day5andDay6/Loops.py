# for item in list_of_items:
  #do something

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):    #10 not included
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum =0
for i in student_heights:
    sum += i
print(round(sum/len(student_heights)))


student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
scores = 0
for i in student_scores:
    if(i>scores):
        scores = i
print(f"The highest score in the class is: {scores}")


sum = 0
for i in range(2,102,2):
    sum += i
    if(i == 100):
        print(str(i)+" = ",end=" ")
    else:
        print(str(i)+" + ",end=" ")
print(sum)