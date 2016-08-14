"""

Ben White
"""

userName = input("Please enter your name: ")

while len(userName) == 0:

    userName = input("Please enter your name")
for i in range(0, len(userName), 2):
    print(userName[i], end='')

