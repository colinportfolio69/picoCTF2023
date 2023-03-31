#!/usr/bin/python3

# Mapping between English alphabet & Atbash cipher

# Create list of alphabetical letters
alphabet = list("abcdefghijklmnopqrstuvwxyz")
    
# Atbash's single substitution key is having all the letters be reversed. So create reverse alphabet
atbash = alphabet[::-1]

# Construct a dictionary matching English letters to Atbash letters.
map = dict(zip(alphabet, atbash))

#Take input from user.
user_input = list(input("What is the encoded message? \n >>>"))
    
#placeholder for decoded message
decoded = []

for i in user_input:
    # Exclude numbers, curly brackets and hyphens, leave only the letters
    if i.isnumeric() == False and i != "{" and i != "}" and i != "_":
        # Convert to lower case for consistency.
        i = i.lower()
        # Add the matching Atbash letter to decoded
        decoded.append(map[i])
    else:
        # Add digits and curly brackets normally
        decoded.append(i)
    
    # convert decoded list back into string
    message = "".join(decoded)

print(f"Your decoded message is: {message}")

