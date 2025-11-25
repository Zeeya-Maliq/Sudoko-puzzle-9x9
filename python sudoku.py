import random

def generate_puzzle():
    solved = [[0]*9 for _ in range(9)]
    for box in range(0, 9, 3):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                solved[box+i][box+j] = nums[i*3+j]
    

    if not fill_sudoku(solved):
        return generate_puzzle()
    
    
    puzzle = [row[:] for row in solved]
    empty_spaces = 0
    target_empty = random.randint(40, 50)
    
    while empty_spaces < target_empty:
        r, c = random.randint(0, 8), random.randint(0, 8)
        if puzzle[r][c] != 0:
            puzzle[r][c] = 0
            empty_spaces += 1
    
    return puzzle, solved

def fill_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in random.sample(range(1, 10), 9):
                    if valid_move(board, i, j, num):
                        board[i][j] = num
                        if fill_sudoku(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def valid_move(board, row, col, num):
  
    if num in board[row]:
        return False
    
    for i in range(9):
        if board[i][col] == num:
            return False
    
    box_row, box_col = row//3*3, col//3*3
    for i in range(3):
        for j in range(3):
            if board[box_row+i][box_col+j] == num:
                return False
    
    return True

def print_board(board):
    print("\n    1 2 3   4 5 6   7 8 9")
    print("  -------------------------")
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("  -------------------------")
        print(r+1, end=" |")
        for c in range(9):
            val = board[r][c] if board[r][c] != 0 else "."
            print(f" {val}", end="")
            if (c + 1) % 3 == 0:
                print(" |", end="")
        print()
    print("  -------------------------")

def play_game():
    puzzle, solution = generate_puzzle()
    original = [row[:] for row in puzzle]
    attempts = 3
    
    print("\n========= 9x9 SUDOKU GAME =========")
    print("Fill empty spots (.) with numbers 1-9")
    print(f"You have {attempts} attempts before game over")
    print("====================================")
    print("\nHOW TO PLAY:")
    print("Enter move as: 'r c n' (row column number)")
    print("Example: 5 3 7 (row 5, column 3, number 7)")
    print("Empty spaces shown as dots (.)")
    print("Type 'solve' to see solution, 'quit' to exit")
    
    while attempts > 0:
        print_board(puzzle)
        
        try:
            user_input = input("\nYour move: ").strip().lower()
            
            if user_input == 'quit':
                print("\nThanks for playing!")
                return
            
            if user_input == 'solve':
                print("\n=== SOLUTION ===")
                print_board(solution)
                return
            
            move_parts = user_input.split()
            
            if len(move_parts) == 3:
                r, c, num = map(int, move_parts)
            elif len(user_input) == 3 and user_input.isdigit():
                r = int(user_input[0])
                c = int(user_input[1])
                num = int(user_input[2])
            else:
                print("Invalid input! Try 'r c n' or 'rcn' format (e.g., '5 3 7' or '537')")
                continue
            
            r -= 1
            c -= 1
            
            
            if not (0 <= r <= 8 and 0 <= c <= 8 and 1 <= num <= 9):
                print("Invalid input! Row and column must be 1-9, number must be 1-9")
                continue
            
            
            if original[r][c] != 0:
                print(f"Cannot change number at row {r+1}, column {c+1}")
                continue
            
            
            if solution[r][c] == num:
                puzzle[r][c] = num
                
                
                if all(0 not in row for row in puzzle):
                    print("\n🎉 CONGRATULATIONS! You solved it! 🎉")
                    print_board(puzzle)
                    return
                
                print("✓ Correct!")
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"✗ Wrong! Attempts left: {attempts}")
                else:
                    print(f"✗ Wrong! No attempts left.")
        
        except ValueError:
            print("Invalid input! Enter numbers only.")
        except Exception as e:
            print(f"Error: {e}")
    
    print("\n=== GAME OVER ===")
    print("Solution was:")
    print_board(solution)

if __name__ == "__main__":
    play_game()
Write a Description for my Github?
