import fileinput
def factorial(n):
    if n == 0 or n == 1: 
        n = 1
    else: 
        n = factorial(n-1)*n
    return n

#Factorial Memo List 
memo = [1]
for i in range(1,101):
    memo.append(factorial(i))

for line in fileinput.input():
    # Strip line
    line = line[:-1]

    # Get total
    total = memo[len(line)]

    # Build count array
    count = [0] * 128
    for c in line:
        count[ord(c)] += 1

    # Remove based on count array
    for i in count:
        if i > 0:
            total //= memo[i]
    print(total)

