from collections import Counter

with open('input.txt', 'r') as file :
    distance = 0

    listx = []
    listy = []
    for line in file :
        values = line.split()
        listx.append(int(values[0]))
        listy.append(int(values[1]))

    counts = Counter(listy)
    indexed_list = {key: value for key, value in counts.items()}

    results = [num * indexed_list.get(num, 0) for num in listx]
    print(sum(results))