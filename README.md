# Password Strength Checker (Programmed in Python)

A simple Python script that rates the strength of a password based on rules:
- Minimum length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

This is one of my first Linux + Python projects, built on Ubuntu and tracked with Git/GitHub.

## How it works
The script checks if the password includes:
- 8+ characters
- at least 1 uppercase letter (A–Z)
- at least 1 lowercase letter (a–z)
- at least 1 number (0–9)
- at least 1 special character (!£$%^&*()?;)

It then outputs a strength rating based on how many of these features it has:
**Very Weak / Weak / Okay / Strong / Very Strong**

If the password is missing anything, it also lists what to add to make it stronger.

## Run it
From the project folder:
python3 password_checker.py
