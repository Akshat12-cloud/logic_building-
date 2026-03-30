#Remove all spaces from a string recursively.
def remove_space(s):
    if len(s)==0:
        return s
    else :
        if s[0]==" ":
            return remove_space(s[1:])
        else:
            return s[0]+remove_space(s[1:])
text=input("enter the string:")
remove=remove_space(text)
print("string after removing spaces:",remove)
        