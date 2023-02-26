with open("01-advent-of-code-challenge/06/sample.in", "r") as f:
    line = f.readline().strip()


for i in range(len(line)):
    if len(set(line[i:i+14]))==14:
        print(i+14)
        break