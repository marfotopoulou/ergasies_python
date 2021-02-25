while True:
    string = input("Give the number of rows: ")
    if string.isdigit():
        rows = int(string)
        break
    else:
        print("Give an integer please...")

cols = rows
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
        array2.append(1)
    for i in range(plithos+1, (rows*cols)+1):
        array2.append(0)

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

    tetrada = 0
    for i in range(rows):
        found = False
        j = 0
        while j < cols - 3:
            if array[i][j] == 1 and array[i][j+1] == 1 and array[i][j+2] == 1 and array[i][j+3]:
                tetrada += 1
                found = True
            if found:
                 j += 4
            else:
                j += 1


    for j in range(cols):
        found = False
        i = 0
        while i < rows - 3:
            if array[i][j] == 1 and array[i+1][j] == 1 and array[i+2][j] == 1 and array[i+3][j] == 1:
                tetrada += 1
                found = True
            if found:
                i += 4
            else:
                i += 1

    for i in range(rows - 3):
         for j in range(cols - 3):
            if array[i][j] == 1 and array[i+1][j+1] == 1 and array[i+2][j+2] == 1 and array[i+3][j+3] == 1:
                tetrada += 1

    for i in range(rows - 4):
        j = cols - 1
        while j >= 3:
            if array[i][j] == 1 and array[i+1][j-1] == 1 and array[i+2][j-2] == 1 and array[i+3][j-3] == 1:
                tetrada += 1
            j -= 1

    total = total + tetrada

print("Total of foursome: " + str(total))
print("Average: " + str(total/100))






















