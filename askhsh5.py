while True:
    string = input("Give the number of rows: ")
    if string.isdigit():
        rows = int(string)
        break
    else:
        print("Give an integer please...")

while True:
    string2 = input("Give the number of columns: ")
    if string2.isdigit():
        cols = int(string2)
        break
    else:
        print("Give an integer please...")

total = 0
for time in range(99):
    array = []
    for i in range(rows):
        array.append([])
        for j in range(cols):
            array[i].append(0)

    """for row in array:
        for elem in row:
            print(elem, end=" ")
        print("")
    
    print("")"""
    if (rows * cols) % 2 == 0:
        plithos = rows * cols // 2
    else:
        plithos = (rows * cols // 2) + 1

    array2 = []

    for i in range(plithos):
        array2.append("S")
    for i in range(plithos+1, (rows*cols)+1):
        array2.append("O")

    import random
    random.shuffle(array2)
    # print(array2)

    z = 0
    for i in range(rows):
        for j in range(cols):
            array[i][j] = array2[z]
            z = z + 1
    print("")
    for row in array:
        for elem in row:
            print(elem, end=" ")
        print("")

    SOS = 0
    for i in range(rows):
        found = False
        j = 0
        while j < cols - 2:
            if array[i][j] == "S" and array[i][j + 1] == "O" and array[i][j + 2] == "S":
                SOS += 1
                found = True
            if found:
                j += 3
            else:
                j += 1

    for j in range(cols):
        found = False
        i = 0
        while i < rows - 2:
            if array[i][j] == "S" and array[i + 1][j] == "O" and array[i + 2][j] == "S":
                SOS += 1
                found = True
            if found:
                i += 3
            else:
                i += 1

    for i in range(rows - 2):
        for j in range(cols - 2):
            if array[i][j] == "S":
                if array[i+1][j+1] == "O" and array[i+2][j+2] == "S":
                    SOS += 1

    for i in range(rows - 3):
        j = cols - 1
        while j >= 2:
            if array[i][j] == "S":
                if array[i+1][j-1] == "O" and array[i+2][j-2] == "S":
                    SOS += 1
            j -= 1

    total = total + SOS

print("Triples of SOS: " + str(total))
average = total/100
print("Average of triples: " + str(average))






