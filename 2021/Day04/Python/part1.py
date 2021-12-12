
def numberParse(s: str):
    return int(s.strip().lstrip("+"))

def createMask(size: int) -> list[list[bool]]:
    return [[False for _ in range(size)] for _ in range(size)]

def isMaskWinning(size: int, mask: list[list[bool]]) -> bool:
    return any( # Row wize
        all(a for a in mask[x]) for x in range(size)
    ) or any( # Column wize
        all(mask[x][y] for x in range(size)) for y in range(size)
    )

def calculateScore(size: int, board: list[list[int]], mask: list[list[bool]]) -> int:
    score = 0
    for x in range(size):
        for y in range(size):
            if mask[x][y] == 0:
                score += board[x][y]

    return score

def day4(input: str):
    parts = input.split("\n\n")
    numbers = map(numberParse, parts[0].split(","))

    boards = []
    for boardText in parts[1:]:
        board = [[numberParse(a) for a in x.split(" ") if a != ""] for x in boardText.split("\n") if len(x) > 0]
        boards.append(board)
    boardSize = len(boards[0])
    masks = [createMask(boardSize) for _ in range(len(boards))]

    finished = []

    for n in numbers:
        for i in range(len(boards)):
            if i in finished:
                continue
            board = boards[i]
            mask = masks[i]
            for x in range(boardSize):
                for y in range(boardSize):
                    mask[x][y] = mask[x][y] or board[x][y] == n
            if isMaskWinning(boardSize, mask):
                score = calculateScore(boardSize, board, mask)
                print("Score:", n * score)
                finished.append(i)

inputFile = open("../input.txt","r")
print(day4(inputFile.read()))


