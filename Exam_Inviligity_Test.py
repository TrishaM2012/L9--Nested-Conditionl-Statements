medical_cause = input("Did you have a medical cause, Y or N?: ")
attendance = int(input("What is the attendance of the student?: "))

if medical_cause == "Y" :
  print("You are allowed")
else:
    if attendance>=75:
       print("You're allowed")
    else:
        print("Not allowed")
  