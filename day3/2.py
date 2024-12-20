def mul(x,y):
    if 0<=x<1000 and 0<=y<1000:
        return x*y

def findMul(list1):
    list1 = list1.split("mul")
    total=0
    list2 = []
    for i in range(len(list1)):
        if list1[i][0] == "(":
            list2.append(list1[i])
    list1 = []
    for i in range(len(list2)):
        comma_index = list2[i].find(',')
        close_index = list2[i].find(')')
        if comma_index == 4:
            digits_of_num1 = 3
        elif comma_index == 3:
            digits_of_num1 = 2
        elif comma_index == 2:
            digits_of_num1 = 1
        else:
            digits_of_num1 = 0


        if close_index - comma_index == 4:
            digits_of_num2 = 3
        elif close_index - comma_index == 3:
            digits_of_num2 = 2
        elif close_index - comma_index == 2:
            digits_of_num2 = 1
        else:
            digits_of_num2 = 0

        if digits_of_num1 and digits_of_num2:
            list1.append(list2[i])
    list2 = []
    del(list1[0])
    for i in range(len(list1)):
        close_index = list1[i].find(')')
        list2.append(list1[i][:close_index+1].removesuffix(')').removeprefix('(').split(','))
    for i in range(len(list2)):
        total += mul(int(list2[i][0]), int(list2[i][1]))
    return total


result = 0
f2 = []
f = open("input", "r")
f = f.read()
f = f.split("do()")
for i in range(len(f)):
    f[i] = "do"+f[i]
    f[i] = f[i].split("don't()")
    for j in range(len(f[i])):
        f[i][j] = f[i][j]
        f2.append(f[i][j])
f=[]
for i in range(len(f2)):
    if f2[i][0] == "d":
        f.append(f2[i])
for i in range(len(f)):
    result += findMul(f[i])
print(result)