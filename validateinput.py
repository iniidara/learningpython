while True:
    age = input('Enter your age: ')
    if age.isdecimal():
        break
    print('Enter a valid age')

while True:
    password = input('Select a new password (letters and numbers only)')
    if password.isalnum():
        break
    print("Enter a valid password")

print("Account creation successful.")