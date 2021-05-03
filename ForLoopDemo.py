# For loop syntax demo
# Interesting to note, the range function is open interval on n ie. n is excluded.

print('Calculating the sum of first n natural numbers:')
n = input('Enter the value of n')
total =0
for i in range(int(n)):
    total = total + i
print(total)
