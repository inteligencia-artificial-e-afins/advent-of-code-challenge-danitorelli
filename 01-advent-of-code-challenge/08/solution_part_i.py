import numpy as np

with open("01-advent-of-code-challenge/08/sample.in", "r") as f:
    lines = f.readlines()
    lines = [entry.strip() for entry in lines]

trees = np.zeros((len(lines), len(lines[0])), dtype=int)
for i, line in enumerate(lines):
    trees[i, :] = np.array(list(line))


visible_trees = 2*len(lines[0]) + 2 *(len(lines)-2)

for i in range(1, trees.shape[0]-1):
    for j in range(1, trees.shape[1]-1):
        tree_column = trees[:, j] - trees[i, j]
        tree_row = trees[i, :] - trees[i, j]
        routes = [tree_row[:j], tree_row[j+1:], tree_column[:i], tree_column[i+1:]]
        if sum(list(map(lambda route: (route<0).all(), routes))) > 0:
            visible_trees += 1
print(visible_trees)
