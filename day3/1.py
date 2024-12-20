
total=0
f2 = []
startmul = False
def mul(x,y):
    if 0<=x<1000 and 0<=y<1000:
        return x*y
f = open("input", "r")
f = f.read()
f = f.split("mul")
for i in range(len(f)):
     if f[i][0] == "(":
         f2.append(f[i])
f = []
for i in range(len(f2)):
    commaIndex = f2[i].find(',')
    closeIndex = f2[i].find(')')
    if commaIndex == 4:
        digits_of_num1 = 3
    elif commaIndex == 3:
        digits_of_num1 = 2
    elif commaIndex == 2:
        digits_of_num1 = 1
    else:
        digits_of_num1 = 0
        
        
    if closeIndex - commaIndex == 4:
        digits_of_num2 = 3
    elif closeIndex - commaIndex == 3:
        digits_of_num2 = 2
    elif closeIndex - commaIndex == 2:
        digits_of_num2 = 1
    else:
        digits_of_num2 = 0
        
    if digits_of_num1 and digits_of_num2:
      f.append(f2[i])  
f2 = []
for i in range(len(f)):
    closeIndex = f[i].find(')')
    f2.append(f[i][:closeIndex+1].removesuffix(')').removeprefix('(').split(','))
for i in range(len(f2)):
    total += mul(f2[i][0], f2[i][1])
print(total)