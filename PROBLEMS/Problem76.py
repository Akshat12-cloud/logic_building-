#Remove all occurrences of a character from a string recursively. 
def remove_char(s, char):
    if not s:
        return ""
    
    first_char = "" if s[0] == char else s[0]
    return first_char + remove_char(s[1:], char)