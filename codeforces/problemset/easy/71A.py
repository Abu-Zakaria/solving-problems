n = int(input())
 
for i in range(n):
    string = input()
    if len(string) < 11:
        print(string)
    else:
        temp = []
        count = 0
        for j in range(len(string)):
            if j == 0 or j == (len(string) - 1):
                temp.append(string[j])
            else:
                count += 1
        print(f"{temp[0]}{count}{temp[1]}")
