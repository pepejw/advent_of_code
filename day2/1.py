safe = []
f = open("input","r")
lines = f.readlines()
for i in range(len(lines)):
     lines[i] = lines[i].removesuffix("\n")
     lines[i] = lines[i].split(" ")
for i in range(len(lines)):
    lastIncreasing = ""
    for j in range(len(lines[i])-1):
        if int(lines[i][j]) - int(lines[i][j+1]) < 0:
            print("inc")
            currentIncreasing = True
        elif int(lines[i][j]) - int(lines[i][j+1]) > 0:
            print("dec")
            currentIncreasing = False
        else:
            print("stays same")
            rowSafe = False
            break
        if lastIncreasing != "":
            if currentIncreasing != lastIncreasing:
                print("at least one line fails")
                rowSafe = False
                break      
        if abs(int(lines[i][j]) - int(lines[i][j+1])) > 3:
            print("gap bigger than 3")
            rowSafe = False
            break
        rowSafe = True
        lastIncreasing = currentIncreasing
    safe.append(rowSafe)
print(safe.count(True))     