# https://codeforces.com/problemset/problem/158/A
n, k = [int(i) for i in input().split(" ")]
scores = [int(i) for i in input().split(' ')]
advancers = 0
for i in range(n):
    if scores[i] >= scores[k - 1] and scores[i] > 0:
        advancers += 1
print(advancers)
