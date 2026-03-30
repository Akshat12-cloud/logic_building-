#Replace all occurrences of a character (say ‘a’ → ‘x’) recursively. 
def replace_char(s, old_char, new_char):
    if len(s) == 0:
        return s
    else:
        if s[0] == old_char:
            return new_char + replace_char(s[1:], old_char, new_char)
        else:
            return s[0] + replace_char(s[1:], old_char, new_char)

text = input("Enter a string: ")
old_character = input("Enter the character to be replaced: ")
new_character = input("Enter the new character: ")

result = replace_char(text, old_character, new_character)
print("String after replacement:", result)