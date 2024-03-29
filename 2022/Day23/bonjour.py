from collections import Counter

grid = set()

directions = [(((-1, 0), (-1, 1), (-1, -1)), (-1, 0)),
              (((1, 0), (1, 1), (1, -1)), (1, 0)),
              (((0,-1), (-1, -1), (1, -1)), (0, -1)),
              (((0, 1), (-1, 1), (1, 1)), (0, 1))]
compass = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

with open('input', 'r') as f:
    for i, line in enumerate(f.readlines()):
        for j, char in enumerate(line.strip()):
            if char == '#':
                grid.add((i, j))

num_moved = 1
r = 0
while num_moved:
    # first half
    proposed_destinations = {}
    for elf_position in grid:
        if not any((elf_position[0] + c[0], elf_position[1] + c[1]) in grid for c in compass):
            continue
        for it in range(4):
            check_directions, proposed_direction = directions[(r + it)%4]
            if not any((d[0] + elf_position[0], d[1] + elf_position[1]) in grid for d in check_directions):
                proposed_destinations[elf_position] = (elf_position[0] + proposed_direction[0], elf_position[1] + proposed_direction[1])
                break
    num_moved = 0
    # second half
    proposed_destinations_counter = Counter(proposed_destinations.values())
    for elf_position, proposed_destination in proposed_destinations.items():
        if proposed_destinations_counter[proposed_destination] == 1:
            grid.remove(elf_position)
            grid.add(proposed_destination)
            num_moved += 1
    print(r, num_moved)
    r += 1
    # # uncomment for part 1
    # if r == 10:
    #     break


# def get_grid(g):
#     for elf in g:
#         min_i, max_i = elf[0], elf[0]
#         min_j, max_j = elf[1], elf[1]
#         break
#     for elf in g:
#         min_i, max_i = min(min_i, elf[0]), max(max_i, elf[0])
#         min_j, max_j = min(min_j, elf[1]), max(max_j, elf[1])


for elf in grid:
    min_i, max_i = elf[0], elf[0]
    min_j, max_j = elf[1], elf[1]
    break
for elf in grid:
    min_i, max_i = min(min_i, elf[0]), max(max_i, elf[0])
    min_j, max_j = min(min_j, elf[1]), max(max_j, elf[1])

height = max_i - min_i + 1
width = max_j - min_j + 1
empty_spaces = width * height - len(grid)
print("empty spaces:", empty_spaces)
print("round number:", r)