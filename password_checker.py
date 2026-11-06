import re


def check_password(pw):
    # each rule maps to whether the password satisfies it
    checks = {
        "at least 8 characters": len(pw) >= 8,
        "an uppercase letter (A-Z)": bool(re.search(r"[A-Z]", pw)),
        "a lowercase letter (a-z)": bool(re.search(r"[a-z]", pw)),
        "a number (0-9)": bool(re.search(r"[0-9]", pw)),
        "a special character (!£$%^&*()?;)": bool(re.search(r"[!£$%^&*()?;]", pw)),
    }

    score = sum(checks.values())
    missing = [rule for rule, passed in checks.items() if not passed]

    levels = {
        0: "Very Weak",
        1: "Very Weak",
        2: "Weak",
        3: "Okay",
        4: "Strong",
        5: "Very Strong",
    }
    return levels[score], missing


password = input("Enter a Password to Test its Strength: ")
rating, missing = check_password(password)

print("Strength:", rating)
if missing:
    print("To make it stronger, add:")
    for item in missing:
        print("  -", item)
