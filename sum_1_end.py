"""Sum of n natural numbers"""
N = int(input('Enter n'))
SUM = 0
I = 1
for I in range(1, N+1, +1):
    SUM += I
    print(SUM)
    