"""Sum of n natural numbers"""
N = int(input('Enter n'))
SUM = 0
I = 1
while I <= N:
    SUM += I
    I += 1
print(SUM)
