# Python Program to build a Simple Calculator using Nested If
choice = int(input("Enter your choice:n"))  # User's choice[1,2,3,4]if (choice>=1 and choice<=4):
print("Enter two numbers: ")
num1 = int(input())
num2 = int(input())

if choice == 1: # To add two numbers
  res = num1 + num2
  print("Result = ", res)

elif choice == 2: # To subtract two numbers
  res = num1 - num2
  print("Result = ", res)

elif choice == 3: # To multiply two numbers
  res = num1 * num2
  print("Result = ", res)

elif choice == 4: # To get quotient with decimal value
  res = num1 / num2
  print("Result = ", res)

elif choice == 5:
    exit()
else:
  print("Wrong input..!!")