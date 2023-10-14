#
# count = 10
# print (count)
# print (type(count))
# # Don't do as below
# same = value = 2
# # instead, do as below
# same = 2
# value = 2
# print (same)
# print (value)
#
# # strings
# name = "Bond"
# print (type(name))
# #changing type of variable from one to another using TYPE CASTING
# #TYPE CASTING
# n = 3
# print (type(n))
#
# # STRING TO INT
#
# st = "44"
# num = int(st)
# print(type(num))
#
# # NUM TO STRING
# num = 38
# print(type(num))
# st = str(num)
# print(type(st))
# print("My age is " +st)
#
#
#
# String Slizing
#     0123456789
# s = "TowerWeekend"
# print(s)  #==> TowerWeekend
# print(s[6])  #==> e
# print(s[0:5])  #==> Tower
# print(s[5:])  #==> Weekend
# print(s*2)  #==>  TowerWeekendTowerWeekend
#
# USING ESCAPE SEQUENCE
# The backslash \ ==> ignore quotes
# str = "the greatest glory in living lies not in never \"falling\", but in raising every time we fall"
# print(str)
#
# # The backslash n  \n ==> new line character
# str = "the greatest glory in living lies not in never \"[falling\", \n but in raising every time we fall"
# print(str)

# grocery_list = ["banana", "potatoes", "cabbage", "tomatoes", "bread", 100]
# print(grocery_list[0])  # ==> print banana
# print(grocery_list[-1])  # ==> print 100
# print(grocery_list[:4])  # ==> prints all except 100
# print("before update " + str(grocery_list)) # ==> print before the update
# grocery_list[3]="corn"  # ==> the update here
# print("after update " + str(grocery_list)) # ==> after update

#=========================DICTIONARIES=========================================

# d = {"name" : "Louis", "emp_id": 1, "Env" : "DevOps"}
# print(d["Env"])
# print(d.keys())
# print(d.values())


# #STUDENTS TOWER WEEKEND BATCH
# students_dict = {
#             "Awa": {"exp": 15, "country": "USA", "specialization": "cars", "visited": ["USA", "Kenya", "Switzerland"]},
#             "Giddy": {"exp":10, "country": "GB", "specialization": "talking", "visited": ["GB", "India", "France"]},
#             "Louis": {"exp":2, "country": "Nigeria", "specialization": "asking", "visited": ["Cameroon", "Nigeria", "Spain"]}
#          }
# print(students_dict)
# print(students_dict.keys())
#
#
# print(students_dict["Awa"]["specialization"])
#
# print(students_dict["Awa"]["specialization"])
#
# print(students_dict["Louis"]["visited"][1])


#=======================PYTHON OPERATORS========================

# x = 618
# print(x%100)




#=========================PYTHON CONDITIONAL==========================

# give_car = False
# user_dict = {
#             "Louis": {"has_license": True, "valid": True, "age": 31, "person_is_insured": True},
#             "Giddy": {"has_license": True, "valid": True, "age": 16, "person_is_insured": True}
#             }
# Care_types = {"sports": ["ferrari", "bentley"], "luxury": ["tesla", "lexus"], "suv": ["range_rover", "rav4"]}
#
# print("Input Username : ")
# user = input()
# if user_dict[user]["has_license"] is True and user_dict[user]["valid"] is True:
#     if user_dict[user]["age"] > 18 and user_dict[user]["person_is_insured"] is True:
#         eligible = "SUV"
#         if user_dict[user]["age"] > 25 and user_dict[user]["age"] < 35:
#             if user_dict[user]["age"] > 30:
#                 eligible = "sports, lexus, SUV"
#             else:
#                 eligible = "sports, SUV"
#         print("Car Eligibility: "+str(eligible))
#         give_car = True
# else:
#     print("Not Eligible for car")
#     give_car = False
# #
# #Assignment
# """
# Age >18
# Person is Insured
# Care_types = {"sports": ["ferrari", "bentley"], ["luxury": "tesla"], "suv": ["range_rover", "rav4"]}
# Sports should be given only if age is > 25 and <35
# Luxury should be given only if age is > 30
#
# Print what sort of car can this person rent?
# """


#======================LOOPING===================================

# count = 0
# while(count <=10):
#     print(count)
#     count+=2
#########################
#
# for item in range(0,11):
#     print(item)



#==========================CALCULATOR===========================

# flag = 1
# while( flag == 1 ):
#     print("\n\n=================CALCULATOR==============\n")
#     print("Choose Operation :")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     choice = int(input("Enter choice 1/2/3/4 :"))
#
#     if choice == 1:
#         num1 = int(input("please enter first number :"))
#         num2 = int(input("please enter second number :"))
#         sum = num1+num2
#         print("SUM OF TWO NUMBERS : "+str(sum))
#     elif choice == 2:
#         num1 = int(input("please enter first number :"))
#         num2 = int(input("please enter second number :"))
#         sub = num1 - num2
#         print("Difference between the two numbers : "+str(sub))
#     elif choice == 3:
#         num1 = int(input("please enter first number :"))
#         num2 = int(input("please enter second number :"))
#         mul = num1 * num2
#         print("Multiplication of the two numbers yields : "+str(mul))
#     elif choice == 4:
#         num1 = int(input("please enter first number :"))
#         num2 = int(input("please enter second number :"))
#         div = num1 / num2
#         print("Division of the two numbers yields :"+str(div))
#     else:
#         print("Invalid operation")
#
#     flag = int(input("Do you wish to continue? Press 1 to continue or 0 to exit : "))


#====MULTIPLYING n NUMBERS TAKEN FROM INPUT====
#
# flag = 1
# while( flag == 1 ):
#     n = float(input("Enter How many numbers you want to multiply : "))
#     mul = 1
#     while (n > 1):
#         num = float(input("Enter the number : "))
#         mul = mul * num
#         n=n-1
#     print("Multiplication of the numbers yields : " + str(mul))
#
#     flag = float(input("Do you wish to continue? Press 1 to continue or 0 to exit : "))
#



# flag = 1
# while( flag == 1 ):

'''
def calculate(n1,n2,op):
    if op == '+':
        result = n1+n2
    elif op == '-':
        result = n1-n2
    elif op == '*':
        result =  n1*n2
    elif op == '/':
        result = n1/n2
    elif op=='^':
        result =  n1**n2
    else:
        raise ValueError('Invalid operator')

    if result.is_integer():
        result = int(result)

    return result

continue_calculating = True
while continue_calculating is True:
    number1 = float(input('Enter first number: '))
    op = input('Enter operator (+,-,*,/,^): ')
    number2 = float(input('Enter second number: '))
    print(number1,op,number2)
    result=calculate(number1,number2,op)
    print('=',result)
    yes_or_no = input('Continue? (y/n): ')
    if yes_or_no == 'n':
        continue_calculating = False
'''
#
#     # flag = float(input("Do you wish to continue? Press 1 to continue or 0 to exit : "))
#
# #print('You entered:',inp)
#
# continue_calculating = True
# while continue_calculating is True:
#     def inp(input_str):
#         n1, op, n2 = input_str.split()
#         n1 = float(n1)
#         n2 = float(n2)
#
#         if op == '+':
#             result = n1+n2
#         elif op == '-':
#             result = n1-n2
#         elif op == '*':
#             result =  n1*n2
#         elif op == '/':
#             result = n1/n2
#         elif op=='^':
#             result =  n1**n2
#         else:
#             raise ValueError('Invalid operator')
#
#         if result.is_integer():
#             result = int(result)
#
#         return result
#
#     user_input = input("START CALCULATION: ")
#     result = inp(user_input)
#     print('Result:', result)
#     yes_or_no = input('WOULD YOU LIKE TO CONTINUE? (y/n): ')
#     if yes_or_no == 'n':
#         continue_calculating = False
#
# # source == https://builtin.com/software-engineering-perspectives/python-calculator

#
# '''RETURN VALUE'''
# def calc(a, b, c):
#     value =a*b+c
#     return value
#
# def another_function():
#     val = calc(20.32, 25, 0)
#     print("From another funcition: " +str(val))
#
# giddy = calc(5, 10, 5)
# print(giddy)
#
# another_function()



import boto3

if __name__ == '__main__':
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances()
    print(response)

