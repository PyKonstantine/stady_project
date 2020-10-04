"""
grid multi place's.
Two input interval on which to be multi place out
"""

a, b = int(input()), int(input())  # вертикаль
c, d = int(input()), int(input())  # горизонталь

for h in range(c, d+1):
    print('\t', h, end='')
print()

for i in range(a, b+1):
    print(i, end='')
    for j in range(c, d+1):
        print('\t', i*j, end='')
    print()
