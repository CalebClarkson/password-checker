import re 

def check_password(pw):
	score = 0

	if len(pw) >= 8:
		score += 1
	if re.search(r"[A-Z]", pw):
		score += 1
	if re.search(r"[0-9]", pw):
		score += 1
	if re.search(r"[!£$%^&*()?;]", pw):
		score += 1

	levels = {
		1: "Very Weak",
		2: "Weak",
		3: "Okay",
		4: "Strong",
		5: "Very Strong"
	}
	return levels[score]

password = input("Enter a Password to Test its Strength: ")
print("Strength: ", check_password(password))
