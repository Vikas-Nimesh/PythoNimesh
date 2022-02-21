import os
os.system("cls")

# '\n' is used to split string in new line
splitString = "This string has been\nsplit over\nseveral\ntimes"
print(splitString)

# '\t' is used to tabbed the string 
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

# This is best and simple way to escape any character
print("""The pet show owner said "No, no, 'e's uh,...he's resting".""")

# This is another way of splitting string
anotherSplitString = """This string has been 
split over 
several
times"""

print(anotherSplitString)

# We can use ' \' to avoid splittng
avoidStringSplit = """This string has been \
split over \
several \
times"""

print(avoidStringSplit)

# We have to used extra '\' to avoud '\t & \n'
studyMaterialPath = "C:\\Users\\theVikasNimesh\\notes"
print(studyMaterialPath)

# Another way
print(r"C:\Users\theVikasNimesh\notes")