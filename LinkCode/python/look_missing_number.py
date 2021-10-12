n = int(input(""))
array = input("").split(" ")
for i in range(1, n+1):
    if str(i) not in array:
        print(i, end=" ")
