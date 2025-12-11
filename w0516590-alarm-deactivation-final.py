alarm_status = "ON"
alarm_activated_status = "ON"
password_attempts = 3

password_list = ["12345", "67890", "34567",]
file = open("passwords.txt", "r")
for line in file:
    password_list.append(line.strip())
file.close()

print("Alarm Status:", alarm_status)
print("Alarm Activated Status:", alarm_activated_status)

while alarm_status == "ON" and password_attempts > 0:

    print("\nEnter your 5 digit Password:")
    user_pass = input()

    if user_pass.isdigit() == False or len(user_pass) != 5:
        print("Invalid Password")
        password_attempts = password_attempts - 1
        print("Attempts left:", password_attempts)
        continue

    if user_pass in password_list:
        print("Password Match")

        alarm_status = "OFF"
        alarm_activated_status = "OFF"
        password_attempts = 3

        print("Alarm Status:", alarm_status)
        print("Alarm Activated Status:", alarm_activated_status)
        break
    else:
        print("Incorrect Password")
        password_attempts = password_attempts - 1
        print("Attempts left:", password_attempts)

if password_attempts == 0:
    alarm_status = "OFF"
    alarm_activated_status = "ON"

    print("\nALARM TRIGGERED!!!")
    print("Alarm Status:", alarm_status)
    print("Alarm Activated Status:", alarm_activated_status)
