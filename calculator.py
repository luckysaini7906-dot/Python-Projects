print("welcome to your calculator")
num=int(input("Enter number , Which is calculate between them as (2,3,4) :"))
if(num==2):
    num1=int(input("Enter first number to calculate : "))
    num2=int(input("Enter secound number to calculate : "))
    user_inst=input("Enter the Instruction which is perform you as (+,-,/,*): ").lower()
    if(user_inst=='+'):
        print("The sum of your number is :",num1+num2)
    elif(user_inst=='*'):
        print("The multiplication of your number is :",num1*num2)
    elif(user_inst=='/'):
        print("The division of your number is :",num1/num2)
    elif(user_inst=='-'):
        print("The subtraction of your number is :",num1-num2)


elif(num==3):
    num1=int(input("Enter first number to calculate : "))
    num2=int(input("Enter secound number to calculate : "))
    num3=int(input("Enter your third number to calculate : "))
    user_inst=input("Enter the Instruction which is perform you as (+,-,/,*): ").lower()
    if(user_inst=='+'):
        print("The sum of your number is :",num1+num2+num3)
    elif(user_inst=='*'):
        print("The multiplication of your number is :",num1*num2*num3)
    elif(user_inst=='/'):
        print("The division of your number is :",(num1/num2)/num3)
    elif(user_inst=='-'):
        print("The subtraction of your number is :",(num1-num2)-num3)

elif(num==4):
    num1=int(input("Enter first number to calculate : "))
    num2=int(input("Enter secound number to calculate : "))
    num3=int(input("Enter your third number to calculate : "))
    num4=int(input("Enter your fourth number to calculate : "))
    user_inst=input("Enter the Instruction which is perform you as (+,-,/,*): ").lower()
    if(user_inst=='+'):
        print("The sum of your number is :",num1+num2+num3+num4)
    elif(user_inst=='*'):
        print("The multiplication of your number is :",num1*num2*num3*num4)
    elif(user_inst=='/'):
        print("The division of your number is :",((num1/num2)/num3)/num4)
    elif(user_inst=='-'):
        print("The subtraction of your number is :",((num1-num2)-num3)-num4)


else:
    print("Unorderd number")