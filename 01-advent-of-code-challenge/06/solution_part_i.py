with open("01-advent-of-code-challenge/06/sample.in", "r") as f:
    line = f.readline().strip()


for i in range(len(line)):
    if len(set(line[i:i+4]))==4:
        print(i+4)
        break
    