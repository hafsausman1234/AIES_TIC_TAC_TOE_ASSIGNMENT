                                                                                            "TIC_TAC_TOE_ASSIGNMENT"

- This project implements a basic "Tic-Tac-Toe" game AI using two different decision-making algorithms: "Minimax" and "Alpha-Beta Pruning". It compares the efficiency of both in terms of move selection time.

- How It Works:

- The game board is represented as a 1D list of 9 squares.
- Two AI algorithms ('minimax' and 'alphabeta') compute the best move for player 'X'.
- Both algorithms simulate optimal play to evaluate the next move.
- Execution time is measured and compared to demonstrate the benefit of pruning.

- Algorithms:
- Minimax: Standard recursive algorithm that explores all possible game states.
- Alpha-Beta Pruning: Optimized version of Minimax that skips branches which won’t affect the final decision.

