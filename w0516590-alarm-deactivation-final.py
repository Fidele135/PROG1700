alarm_status = "ON"
alarm_activated_status = "ON"

def load_passwords():
    defaults = ["12345", "67890", "34567"]
    try:
        with open("passwords.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    defaults.append(line)
    except FileNotFoundError:
        pass
    return defaults

password_list = load_passwords()

print("Alarm Status:", alarm_status)
print("Alarm Activated Status:", alarm_activated_status)

while alarm_status == "ON":
    password_attempts = 3

    while password_attempts > 0:
        user_pass = input("\nEnter your 5 digit Password: ").strip()

        if not user_pass.isdigit() or len(user_pass) != 5:
            print("Invalid Password format. Use 5 digits.")
            password_attempts -= 1
            print("Attempts left:", password_attempts)
            continue

        if user_pass in password_list:
            print("Password Match")
            alarm_status = "OFF"
            alarm_activated_status = "OFF"
            print("Alarm Status:", alarm_status)
            print("Alarm Activated Status:", alarm_activated_status)
            break
        else:
            print("Incorrect Password")
            password_attempts -= 1
            print("Attempts left:", password_attempts)

    if alarm_status == "OFF":
        break
    
    print("\nALARM TRIGGERED!!!")
    alarm_status = "ON"
    alarm_activated_status = "ON"
    print("Alarm Status:", alarm_status)
    print("Alarm Activated Status:", alarm_activated_status)
    print("\nSystem resetting... Get ready to enter your password again.\n")
