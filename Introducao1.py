andares =  0

print("\n 1\n 2\n 3\n 4\n 5\n 6\n 7\n 8\n 9\n 10\n 11\n 12\n 14\n 15\n 16\n 17\n 18\n 19\n 20 \n" )

for i in range(1, 21):
    if i == 13:
        continue
    print(i)


print()

for i in range(20, 0, -1):
    if i == 13:
        continue
    print(i)


print()

while andares < 20:
    andares = andares +1
    if andares == 13:
        continue
    print(andares)