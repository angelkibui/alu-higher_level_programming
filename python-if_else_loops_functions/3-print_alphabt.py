#!/usr/bin/python3
for letter in range(97, 123):
    if letter != 101 and letter != 113:  # 101 is 'e', 113 is 'q'
        print(chr(letter), end="")
print()
