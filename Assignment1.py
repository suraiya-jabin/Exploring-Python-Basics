#Task 1 starts from here (Variable manipulation)

name = "Suraiya Jabin" #assigned name
age = 24   #assigned age

print ("\nMy name is " + name + " and I am " + str(age) + "years old.\n\n") #Task 1 ends here


#Task 2 starts from here (Data Types and Type Conversion)
num1 = 10     #integer number
num2 = 10.0   #float number

num1_float = float(num1) #type casting to change data type
num2_int = int(num2)     #type casting to change data type

print("Integer number: " + str(num1) + "\nFloat Number: " +  str(num2) + 
      "\nInteger Number coverted to Float Number: " + str(num1_float) + 
      "\nFloat Number coverted to Integer Number \n" +  str(num2_int))

#Task 2 ends here

#Task 3 starts from here (String Manipulation)
new_sentence = "Python programming is Fun!"

print("Length of Sentence is: " + str(len(new_sentence)) )#printing length
print("8th Character of Sentence is: " + str(new_sentence[8]) )#printing 8th Character of Sentence

substring = new_sentence [0:6]
print(substring)

print("I enjoy it " + substring) #3rd problem ends here

#Task 4 starts from here (Lists and List manipulation)
fruits = ["apple", "banana", "cherry", "date"]

fruits.append("grape") #adding new value to list
fruits.remove("banana") #removing a value from list

print(len(fruits)) #finding Length
sliced_fruits = fruits[2:4] #slicing 
print(sliced_fruits)

extra_fruits = ["kiwi", "lemon"]
combined_fruits = sliced_fruits + extra_fruits
print(combined_fruits)  #Task 4 ends here

#Task 5 starts from here (Conditional Statements)
num = int(input("Please enter a number to check odd or even: "))
if num % 2 == 0: #condition
      print("\nEven") #if the condition is true
else:
      print("\nodd") #condition false

#Task 6 starts from here (Loops)

for num in range(1, 11): #iteraion 
    print(num)


#Task 7 starts from here (Functions)

def calculate_square(): #this is a function to calculate square

  number = int(input("Please enter an integer number: "))
  square_number = number**2 #square calculation

  print(square_number)

calculate_square() #function call

def is_prime(): #function

  num = int(input("Enter a number to check Prime number: "))

  # define a flag variable
  flag = False

  if num == 1:
      print(num, "is not a prime number")
  elif num > 1:
    # check for factors
      for i in range(2, num):
            if (num % i) == 0:
            # if factor is found, set flag to True
             flag = True
            # break 
            break

    # check if flag is True
      if flag:
          print(num, "is not a prime number")
      else:
        print(num, "is a prime number")

is_prime() #function call

#Task 8 starts from here (Dictionaries)
dictionary = dict() #Dictionaries

dictionary ['name'] = "Suraiya Jabin"
dictionary ['age'] = 24
dictionary ['grade'] = 4.00

print(dictionary)

dictionary ['course'] = "CSE" #Adding a new key "course" with a value
print(dictionary)
print("\n")

# printing dictionary keys one by one
for value in dictionary:
    print(value)





 


