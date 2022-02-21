import os
os.system("cls")

letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25::-1]
print(backwards)

#mini challenge to print 'qpo'
qpo_string = letters[16:13:-1]
print(qpo_string)


#mini challenge to print 'edcba'
edcba_string = letters[4::-1]
print(edcba_string)


#mini challenge to produce last 8 char in reverse order
reverse_8_string = letters[25:17:-1]
print(reverse_8_string)