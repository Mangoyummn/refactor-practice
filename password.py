# Instructions for Students:

# Refactor this code by creating a validate_password(password) function.
# Extend it to check for additional rules like special characters.
def validate_password(password):
  if len(password) >= 8:
    if any(char.isdigit() for char in password):
        if any(char.isupper() for char in password):
            print("Strong password")
        else:
            print("Password needs an uppercase letter")
    else:
        print("Password needs a number")
  else:
    print("Password is too short")