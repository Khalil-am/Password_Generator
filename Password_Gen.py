import random
import string


def generate_password(min_length, numbers=True, special_charecters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    charecters = letters
    if numbers:
        charecters += digits
    if special_charecters:
        charecters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(charecters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_charecters:
            meets_criteria = meets_criteria and has_special

    return pwd;



print("""
 __    __    ___  _        __   ___   ___ ___    ___      ______   ___       ___ ___  __ __      ____   ____  _____ _____ __    __   ___   ____   ___         ____    ___  ____  
|  |__|  |  /  _]| |      /  ] /   \ |   |   |  /  _]    |      | /   \     |   |   ||  |  |    |    \ /    |/ ___// ___/|  |__|  | /   \ |    \ |   \       /    |  /  _]|    \ 
|  |  |  | /  [_ | |     /  / |     || _   _ | /  [_     |      ||     |    | _   _ ||  |  |    |  o  )  o  (   \_(   \_ |  |  |  ||     ||  D  )|    \     |   __| /  [_ |  _  |
|  |  |  ||    _]| |___ /  /  |  O  ||  \_/  ||    _]    |_|  |_||  O  |    |  \_/  ||  ~  |    |   _/|     |\__  |\__  ||  |  |  ||  O  ||    / |  D  |    |  |  ||    _]|  |  |
|  `  '  ||   [_ |     /   \_ |     ||   |   ||   [_       |  |  |     |    |   |   ||___, |    |  |  |  _  |/  \ |/  \ ||  `  '  ||     ||    \ |     |    |  |_ ||   [_ |  |  |
 \      / |     ||     \     ||     ||   |   ||     |      |  |  |     |    |   |   ||     |    |  |  |  |  |\    |\    | \      / |     ||  .  \|     |    |     ||     ||  |  |
  \_/\_/  |_____||_____|\____| \___/ |___|___||_____|      |__|   \___/     |___|___||____/     |__|  |__|__| \___| \___|  \_/\_/   \___/ |__|\_||_____|    |___,_||_____||__|__|
                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                   
""")
min_length = int(input("Enter the minimum length: "))
has_numbers = input("do you want it to have numbers (y/n) ? : ").lower() =="y"
has_special = input("do you want it to have special characters (y/n) ? : ").lower() =="y"
pwd = generate_password(min_length,has_numbers, has_special)
print("The generated password is: ",pwd)
