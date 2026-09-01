from datetime import datetime
print("Hey ! I am AI chatbot 😎 :) ")
current_time=datetime.now().hour
if current_time<12:
    print("Good morning! 🌞 ")
elif current_time<18:
    print("Good Afternoon! 🌞 ")
else:
    print("Good Evening! 😊")
qus=input().lower()

if (qus=='hi' or qus=='hello'):
    print("Hello ! what can i help you 😊:")
    msg1=input().lower()
    if (msg1=='python'):
        print("python is a programming language")
    elif(msg1=='you'):
        print("I am fine😊, and you")
elif(qus=='bye'):
    print("Thanks! Have a nice day 😊 ")
    




