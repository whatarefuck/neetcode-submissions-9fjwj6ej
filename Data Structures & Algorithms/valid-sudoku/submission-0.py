from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = defaultdict(list)
        get_box = lambda x, y: boxes[(y // 3) * 3 + (x // 3) + 1]

        y_lines = [[] for _ in range(9)]
        for y in range(9):
            x_line = []
            for x in range(9):
                num = board[y][x]

                #skip empty cells
                if num == ".":
                    continue

                #horizontal line duplicate check
                if num in x_line:
                    print(f"{num} in x_line")
                    return False
                x_line.append(num)

                #vertical line duplicate check
                y_line = y_lines[x]
                if num in y_line:
                    print(f"{num} in y_line")
                    return False
                y_line.append(num)

                #box duplicate check
                if num in get_box(x, y):
                    return False
                get_box(x, y).append(num)
        
        return True

            