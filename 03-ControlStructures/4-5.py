###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if char != ' ':
        # read the character's code (use ord())
        # add one to the character's code
        new_char_code = ord(char) + 1
        # replace new character code with its
        # corresponding character (use chr())
        new_char = chr(new_char_code)
        # add encrypted character to encrypted text
        encrypted_text += new_char
    else:
        encrypted_text += ' '

print(f'Plain text: {plain_text}')
print(f'Encrypted text: {encrypted_text}')