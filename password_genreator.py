import random
import string

print("\n Hello ! Welcome To Random Password Generator")

while True:
    
    legnth=int(input("\n Enter Your Legnth Of Password :"))
    password=""

    if legnth>=10:
        characters=string.ascii_letters+string.digits+string.punctuation
        # for i in range(legnth):
        #     password += random.choice(characters)
        # print("Your Password Is :",password)
        pass_gen=random.sample(characters,legnth)
        password=" ".join(pass_gen)

        print("\n Your Password Is :",password)
    else:
        print("\n Please Enter Your Legnth Which is Grater Than Or Equals To Ten(10) , Thankyou !")
 