with open('input.txt', 'r') as file :
    distance = 0

    listx = []
    listy = []
    for line in file :
        values = line.split()
        listx.append(int(values[0]))
        listy.append(int(values[1]))
    
    listx.sort()
    listy.sort()

    index = 0
    for value in listx :
        values = [value, listy[index]]
        diff = int(max(values) - min(values))
        distance = distance + diff
        index = index + 1

    print(distance)