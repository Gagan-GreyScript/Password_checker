def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in "!@#$%^&*()" for char in password):
        strength += 1

    return strength

if __name__ == "__main__":
    pwd = input("Enter a password to check its strength: ")
    result = check_password_strength(pwd)
    print(f"Password Strength Score: {result}/4")
