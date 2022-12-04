import json
import queue

forbidden_c = [2, 4, 6, 8]
COSTS = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

class Board:

    def __init__(self, other):
        if isinstance(other, Board):
            self.corridor = list(other.corridor)
            self.rooms = [list(r) for r in other.rooms]
            self.energy_used = other.energy_used
        else:
            lines = other.splitlines()
        
            self.corridor = [None for x in lines[1] if x == "."]
            self.rooms = [
                [ lines[3][3], lines[2][3] ],
                [ lines[3][5], lines[2][5] ],
                [ lines[3][7], lines[2][7] ],
                [ lines[3][9], lines[2][9] ],
            ]
        
            self.energy_used = 0
    
    def print(self):
        print(self.energy_used)
        print("#############")
        print("#", end="")
        for x in self.corridor:
            if x == None:
                print(".", end="")
            else:
                print(x, end="")
        print("#")
        print("###", end="")
        for c in range(4):
            print(self.rooms[c][1] or ".", end="#")
        print("##")

        print("  #", end="")
        for c in range(4):
            print(self.rooms[c][0] or ".", end="#")
        print("#")
        print("  #########")
        pass
        
    def short_str(self):
        return str(self.corridor) + str(self.rooms)

    def __hash__(self):
        return hash(self.short_str())
    
    def create_moves(self, valid = True):
        moves: list[Board] = []
        # Rooms
        for r in range(0, 4):
            top = 1
            bottom = 0
            # Out
            if self.rooms[r][top] != None:
                if self.corridor[2 + 2*r] == None:
                    if self.corridor[1 + 2*r] == None:
                        child = Board(self)
                        moves.append(child)
                        child.corridor[1 + 2*r] = self.rooms[r][top]
                        child.rooms[r][top] = None
                        child.energy_used += COSTS[self.rooms[r][top]] * 2
                    if self.corridor[3 + 2*r] == None:
                        child = Board(self)
                        moves.append(child)
                        child.corridor[3 + 2*r] = self.rooms[r][top]
                        child.rooms[r][top] = None
                        child.energy_used += COSTS[self.rooms[r][top]] * 2
            elif self.rooms[r][bottom] != None:
                child = Board(self)
                moves.append(child)
                child.rooms[r][top] = self.rooms[r][bottom]
                child.rooms[r][bottom] = None
                child.energy_used += COSTS[self.rooms[r][bottom]]
            # In
            if self.rooms[r][1] != None:
                pass
        # 0 to 1
        if self.corridor[0] != None and self.corridor[1] == None:
            child = Board(self)
            moves.append(child)
            child.corridor[1] = self.corridor[0]
            child.corridor[0] = None
        # Last to avant dernier
        if self.corridor[-1] != None and self.corridor[-2] == None:
            child = Board(self)
            moves.append(child)
            child.corridor[-2] = self.corridor[-1]
            child.corridor[-1] = None
            
        for c in range(0, len(self.corridor)):
            if self.corridor[c] == None:
                continue
            for d in [-1, 1]:
                if c + d < 0 or c + d >= len(self.corridor):
                    continue
                if c + d in forbidden_c:
                    d *= 2
                if self.corridor[c + d] == None:
                    child = Board(self)
                    moves.append(child)
                    child.corridor[c + d] = self.corridor[c]
                    child.corridor[c] = None
        return moves
    
    def solved(self) -> bool:
        for i, letter in enumerate(['A', 'B', 'C', 'D']):
            if self.rooms[i][0] != letter:
                return False
            if self.rooms[i][1] != letter:
                return False
        return True

def explore(startB):
    founds = {
        startB.short_str(): startB
    }
    q = queue.SimpleQueue()
    q.put(startB.short_str())
    
    i = 0
    while not q.empty():
        i += 1
        """
        mk, m = min(
            ((i[0], i[1][1]) for i in founds.items() if i[1][0]),
            key = lambda b: b[1].energy_used
        )
        """
        mk = q.get(False)
        m = founds[mk]
        
        if m.solved():
            print("FOUND!!!!!=======")
            m.print()
            return

        for h in m.create_moves():
            k = h.short_str()
            if k not in founds or founds[k].energy_used > h.energy_used:
                founds[k] = h
                q.put(k)

        if i % 10000 == 0:
            print("Parcoured =", len(founds))
            print("Its=", i)
            m.print()
            print("----------------------")

    print("FAILED!!!!!")
    print("Parcoured =", len(founds))
    print("Its=", i)
    m.print()

f = open("../input.txt")
b = Board(f.read())
f.close()

print("Start:")
b.print()
print("----------------")

b = b.create_moves()[0]

print("moves:")
for m in b.create_moves():
    m.print()

#explore(b)

