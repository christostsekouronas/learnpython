#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
# if I want to print z...a then in line 4 I should write : backwards = letters[25::-1], so the slicing starts printing from 25 backwards to the start INCLUDING the start

# create a slice that produces the characters qpo
print(letters[16:13:-1])

# slice the string to produce edcba
print(letters[4::-1])

# slice the string to produce the last 8 characters, in reverse order
print(letters[25:17:-1])
# also I could write print(letters[:-9:-1])

print(backwards)

print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])
