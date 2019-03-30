import queue

#Menentukan sebuah pilihan langkah valid / tidak
def validMove(labirin, langkah):
    for j, row in enumerate(labirin):
        for i,col in enumerate(row):
            if col == "M":
                x1 = i
                y1 = j
                break

    x = x1
    y = y1
    #print(x)
    #print(y)

    for i in langkah:
        if i == "U":
            y -= 1
        elif i == "D":
            y += 1
        elif i == "L":
            x -= 1
        elif i == "R":
            x += 1

    if not ( 0<= x < len(labirin[0]) and 0 <= y < len(labirin)):
        #print("FALSE")
        return False
    elif labirin[y][x] == "#":
        #print("FALSE")
        return False

    #print("TRUE")
    return True

#Menentukan apakah sudah mencapai titik akhir (S)
def endPoint(labirin, langkah):
    for j, row in enumerate(labirin):
        for i,col in enumerate(row):
            if col == "M":
                x1 = i
                y1 = j
                break

    x = x1
    y = y1
    #print(x)
    #print(y)

    for i in langkah:
        if i == "U":
            y -= 1
        elif i == "D":
            y += 1
        elif i == "L":
            x -= 1
        elif i == "R":
            x += 1
    if labirin[y][x] == "S":
        changePath(labirin,langkah)
        print("langkah yang didapat " + langkah)
        printMap(labirin)
        return True
    #print("Tidak sampai")
    return False

#Membuat labirin
def buatLabirin():
    labirin = []
    labirin.append(["#", "#", "M", "#"])
    labirin.append(["#", " ", " ", "#"])
    labirin.append([" ", "#", " ", "#"])
    labirin.append(["S", "#", " ", "#"])
    labirin.append([" ", "#", " ", "#"])
    labirin.append(["#", "#", "#", "#"])

    return labirin

#Memberikan tanda + pada jalan yang dipilih
def changePath(labirin, langkah):
    for j, row in enumerate(labirin):
        for i,col in enumerate(row):
            if col == "M":
                x1 = i
                y1 = j
                break

    x = x1
    y = y1
    #print(x)
    #print(y)

    for i in langkah:
        if i == "U":
            y -= 1
        elif i == "D":
            y += 1
        elif i == "L":
            x -= 1
        elif i == "R":
            x += 1
        if labirin[y][x] != "S":
            labirin[y][x] = "+"


    return labirin

#Mencetak labirin beserta path yang dipilih
def printMap(labirin):
    for j, row in enumerate(labirin):
        for i, col in enumerate(row):
            print(col + " ",end="")
        print()

def poscount(labirin):
    steps = 0
    for j, row in enumerate(labirin):
        for i,col in enumerate(row):
            if col == " ":
                steps +=1
    steps+=4
    return steps

#Testing Program

#1. Membuat labirin
labirin = buatLabirin()
#2. Membuat Queue untuk BFS
bfs = queue.Queue()
bfs.put("")
#3. Membuat variabel untuk menyimpan
#kemungkinan langkah

posstep = ""
totstep = poscount(labirin)

#Proses pencarian Jalur
while not endPoint(labirin,posstep):
    if len(posstep) > totstep:
        print("no Valid Path")
        exit(2)

    posstep = bfs.get()
    for direction in ["U","D","L","R"]:
        choice = posstep + direction
        if validMove(labirin,choice):
            bfs.put(choice)

exit(0)

