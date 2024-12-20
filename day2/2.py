def testline(line):

    lastincreasing = ""
    rowsafe = True
    for j in range(len(line)-1):
        if int(line[j]) - int(line[j+1]) < 0:
            currentincreasing = True
        elif int(line[j]) - int(line[j+1]) > 0:
            currentincreasing = False
        else:
            rowsafe = False
            break
        if lastincreasing != "":
            if currentincreasing != lastincreasing:
                rowsafe = False
                break
        if abs(int(line[j]) - int(line[j+1])) > 3:
            rowsafe = False
            break
        rowsafe = True
        lastincreasing = currentincreasing
    return rowsafe

safe = []
f = open("input","r")
lines = f.readlines()
for i in range(len(lines)):
     lines[i] = lines[i].removesuffix("\n").split(" ")
for i in range(len(lines)):
    line = lines[i]
    rowSafe = testline(line)
    oldLine = []
    for item in line:
        oldLine.append(item)
    if not rowSafe:
        for j in range(len(line)):
            del(line[j])
            rowSafe = testline(line)
            if rowSafe:
                break
            line = []
            for item in oldLine:
                line.append(item)
    safe.append(rowSafe)
                
        
    

print(safe.count(True))     