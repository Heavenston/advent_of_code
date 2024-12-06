import random
import time

import networkx as nx

start_time = time.time()

Gr = nx.Graph()
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        a = line.split(':')[0]
        for b in line.split(':')[1].strip().split(' '):
            Gr.add_edge(a, b, capacity=1)

while True:
    nodes = list(Gr.nodes())
    a, b = random.choices(nodes, k=2)
    if a == b:
        continue
    cut, partition = nx.minimum_cut(Gr, a, b)
    if cut == 3:
        print(len(partition[0]) * len(partition[1]))
        end_time = time.time()
        break

execution_time = end_time - start_time

print(f"{execution_time * 1000} ms")
