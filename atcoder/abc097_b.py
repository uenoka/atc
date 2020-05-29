#abc097_b
X = int(input())
ans = 0
for i in range(X+1):
    for j in range(2,10):
        if i**j<=X and ans < i**j:
            ans =i**j
print(ans)