print("Hello World")

# VARIABLE - a  way to store a single piece of data.
# ex: Score and Health in games. 

# nameofvariable = value 
score = 0 
name = "Spongebob"
health = 100.405679 

print(name)

#CONDITIONALS - if/else statements used for decision-making.  

if score == 5:
  print("your score is 5") 
else:
  print("your score is 0")

num = 30  

# Create an if/else statement that will print 
# whether num is less than or greater than 30. 

if num > 30:
  print("greater than 30")
elif num == 30:
  print("num equals 30")
else:
  print("less than 30")

# LOOPS: a way to repeat code for a given amount of times or until a condition is met. 

for i in range(5):
  print("smelly cat")

count = 0
while (count < 9):
  print("the count is: " + str(count)) 
  # count = count + 1
  count += 1


##################################

name = input("What is your name?")
print("Hello" + name)

# Variable name discussion
# I want to create a variable that keeps track of how many avenger's team members there are at headquarters. What should we name the variable? Go ahead and write the name of the varaible into the chat. 

#list
avengers = ["black widow", "ironman"]

#var 
avengers_count = 4


# Write a program that asks the user for their full name, age, and their favorite activity. Store full name age and activity into variables and display them back to the user.

num1 = int(input("Please enter a number."))
num2 = int(input("Please enter another number."))
print("The sum of your two numbers is: {}".format(num1+num2))

print("Hello!")
fullName = input("What is your first and last name?")

age = input("How old are you?")
#ask for the user's favorite activity.

FavAct = input("What is your favorite thing to do in your free time?")

print("Your name is" + fullName) 
# print out user's age in a sentence.
# print out the user's favorite activity in a sentence.
print("you are" + age + "Years Old")

print("And your favorite activity is" + FavAct) 

print("Very interesting...")