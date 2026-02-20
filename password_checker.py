def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in "!@#$%^&*()-_=+[]{};:,.<>/?" for char in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Moderate"
    else:
        return "Strong"


def main():
    print("Password Strength Checker")
    password = input("Enter a password: ")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")


if __name__ == "__main__":
    main()
