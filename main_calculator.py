# count = 10
# print(count)
# print(type(count))
# same = 2
# value = 2
# print(same)
# print(value)
# name = "Bond"
# print(type(name))


# Type Casting : Changes the type of variable
# num = 20          #INTEGER TYPE
# print(type(num))
# st = str(num)      #STRING TYPE
# print(type(st))
# print("My age is "+st)

# STRING TO INT
# st = "12"
# num = int(st)
# print(type(num))
# 01234567891011
# s = "TowerWeekend"
# print(s)
# print(s[:2])
# str = "the greatest glory in living lies not in never \"falling\", \n but in rising every time we fall"
# print(str)
# grocery_list = ["banana", "potatoes", "cabbage", "tomatoes", "bread", 100]
# print("Before Update " + str(grocery_list))
# grocery_list[3]="corn"
# print("After Update " + str(grocery_list))

# grocery_tuple = ("banana", "potatoes", "cabbage", "tomatoes", "bread", 100)
# grocery_tuple[3]="corn"
# print("After Update " + str(grocery_tuple))


# ==============DICTIONARIES================
# d = {"name": "Showmik", "emp_id": 1, "department": "DevOps"}
# print(d["department"])
# print(d.keys())
# print(d.values())
# STUDENTS TOWER WEEKEND BATCH
# students_dict = {
#             "Awa": {"exp": 15, "country": "USA", "specialization": "cars", "visited": ["USA", "Kenya", "Switzerland"]},
#             "Giddy": {"exp":10, "country": "GB", "specialization": "talking", "visited": ["GB", "India", "France"]},
#             "Louis": {"exp":2, "country": "Nigeria", "specialization": "asking", "visited": ["Cameroon", "Nigeria", "Spain"]}
#          }
#
# print(students_dict["Giddy"]["specialization"])
# print(students_dict["Louis"]["country"])

# print(students_dict["Louis"]["visited"][1])

# =============CONDITIONALS ================
'''
    Age > 18;
    Person is Insured.
    -------------------
    car_types = {"sports": ["ferrari", "bentley"], "luxury": ["lexus", "tesla"], "suv": ["range", "rav4"]}
    Sports should be given only if age is > 25 and < 35
    Luxury should be given only if age is > 30
    -------------------
    Print what sort of car can this person rent.
'''
#
# give_car = False
# user_dict = {
#              "showmik": {"has_license": True, "valid": True, "age": 29, "is_insured": True},
#              "Giddy": {"has_license": True, "valid": True, "age": 34, "is_insured": True}
#             }
# car_types = {"sports": ["ferrari", "bentley"], "luxury": ["lexus", "tesla"], "suv": ["range", "rav4"]}
#
# print("Input Username : ")
# user = input()
# if user_dict[user]["has_license"] is True and user_dict[user]["valid"] is True:
#     if user_dict[user]["age"] > 18 and user_dict[user]["is_insured"] is True:
#         eligible = car_types["suv"]
#         if 25 < user_dict[user]["age"] < 35:
#             eligible.extend(car_types["sports"])
#             if user_dict[user]["age"] > 30:
#                 eligible.extend(car_types["luxury"])
#
#         print("Car Eligibility : "+str(eligible))
#         give_car = True
# else:
#     print("Not Eligible for a car")
#     give_car = False



# ===================LOOPING ======================
#
# grocery_list = ["banana", "potatoes", "cabbage", "tomatoes", "bread"]
# Either go over a range of number
# Or go over each item
# count = 1
# for item in grocery_list:
#     print(str(count) + " Item " + item)
#     count += 1
# print("===========================")
# for index in range(0,5):
#     print(str(index+1) + " Item " + grocery_list[index])
# for item in "Chimezie":
#     print(item)

# count = 0
# while(count <= 10):
#     print(count)
#     count += 1
#
# for item in range(0,11):
#     print(item)

#==================CALCUATOR=======================
# flag = 1
# while( flag==1 ):
#     print("\n\n=============CALCULATOR===================\n")
#     print("Choose Operation : ")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     choice = int(input("Enter Choice 1/2/3/4 : "))
#
#     if choice == 1:
#         num1 = int(input("Please enter first number : "))
#         num2 = int(input("Please enter second number : "))
#         sum = num1+num2
#         print("SUM OF TWO NUMBERS : "+str(sum))
#     elif choice == 2:
#         num1 = int(input("Please enter first number : "))
#         num2 = int(input("Please enter second number : "))
#         sub = num1 - num2
#         print("Difference between the two numbers : "+str(sub))
#     elif choice == 3:
#         n = int(input("Enter How many numbers you want to multiply"))
#         num1 = int(input("Please enter first number : "))
#         num2 = int(input("Please enter second number : "))
#         mul = num1 * num2
#         print("Multiplication of the two numbers yields : "+str(mul))
#     elif choice == 4:
#         num1 = int(input("Please enter first number : "))
#         num2 = int(input("Please enter second number : "))
#         div = num1 / num2
#         print("Division of the two numbers yields :"+str(div))
#     else:
#         print("Invalid option chosen")
#
#     flag = int(input("Do you wish to continue? Press 1 to continue or 0 to exit : "))
#

# MULTIPLYING n NUMBERS TAKEN FROM INPUT

# n = int(input("Enter How many numbers you want to multiply"))
# mul = 1
# while (n > 0):
#     num = int(input("Enter the number : "))
#     mul = mul * num
#     n=n-1
# print("Multiplication of the numbers yields : " + str(mul))

'''
//          HOMEWORK CALCULATOR 25th September

INPUT : NUM1 <OPERATION> NUM2
Eg: 25 * 5
OUTPUT : 125

s = "2 seconds 5"
print(s.split(" "))
['2', 'seconds', '5']


'''
