

print("\n\n=================CALCULATOR==============\n")
print("Choose Operation :")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter choice 1/2/3/4 :"))



if choice == 1:
    num1 = int(input("please enter first number :"))
    num2 = int(input("please enter second number :"))
    sum_result = num1 + num2

    print("sum of", num1, "and", num2, "is", sum_result)

    print("SUM OF TWO NUMBERS : "+str(sum))
elif choice == 2:
    num1 = int(input("please enter first number :"))
    num2 = int(input("please enter second number :"))
    sub = num1 - num2
    print("Difference between the two numbers : "+str(sub))
elif choice == 3:
    num1 = int(input("please enter first number :"))
    num2 = int(input("please enter second number :"))
    mul = num1 * num2
    print("Multiplication of the two numbers yields : "+str(mul))
elif choice == 4:
    num1 = int(input("please enter first number :"))
    num2 = int(input("please enter second number :"))
    div = num1 / num2
    print("Division of the two numbers yields :"+str(div))
else:
    print("Invalid operation")


