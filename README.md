Terminal Sudoku Game (Python)
A fully-playable 9×9 Sudoku game in the terminal, featuring automatic puzzle generation, input validation, multiple difficulty levels, and a built-in solver. The game creates a valid Sudoku board, removes numbers to form a playable puzzle, and guides the user through completing it with limited attempts.


✨ Features
✔️ Random Sudoku puzzle generator using backtracking
✔️ Guaranteed valid solution
✔️ Medium-difficulty puzzles (40–50 empty cells)
✔️ User-friendly terminal UI with clean board formatting
✔️ Input validation (supports both r c n and rcn formats)
✔️ Three attempts before game over
✔️ Instant solution reveal (solve command)
✔️ Prevents modifying original puzzle cells

🎮 How It Works
The generator first fills the diagonal 3×3 boxes.
It completes the board using a randomized backtracking solver.
It removes random cells while keeping the puzzle solvable.
