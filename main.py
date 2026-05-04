board = []
for i in range(1,10):
    board.append(i)
logs = []
value = 'x'
move = 0
win = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
is_win = False
def draw():
    print("="*13)
    for i in range(3):
        print(f"| {board[i*3]} | {board[(i*3)+1]} | {board[(i*3)+2]} |")
        print("="*13)
while True:
    try:
        draw()
        user = int(input(f"{value} > "))
        if user < 1:
            print("Введите число от 1 до 9")
            continue
        if user in logs:
            continue
        if move % 2 == 0:
            board[user-1] = "x"
            value = 'o'
        else:
            board[user-1] = "o"
            value = 'x'
    
        logs.append(user)
        move += 1
        for i in win:
            if board[i[0]-1] == board[i[1]-1] == board[i[2]-1] == "x":
                board[i[0]-1] = "X"
                board[i[1]-1] = "X"
                board[i[2]-1] = "X"
                text = "Крестики победили"
                is_win = True
                break
            elif board[i[0]-1] == board[i[1]-1] == board[i[2]-1] == "o":
                board[i[0]-1] = "O"
                board[i[1]-1] = "O"
                board[i[2]-1] = "O"
                text = "Нолики победили"
                is_win = True
                break
        if len(logs) == 9 and is_win == False:
            text = "Ничья"
            break
        if is_win:
            break
    except:
        print("Введите число от 1 до 9")
        continue
draw()
print(text)
