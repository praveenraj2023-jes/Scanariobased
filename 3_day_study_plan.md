# 3-Day AI Lab Preparation Strategy

Since you have **three days** to prepare, we can break down the topics logically to avoid overwhelming yourself. The strategy is to tackle fundamental concepts on Day 1, constraint satisfaction and logic on Day 2, and advanced planning and recursion on Day 3.

The good news is that many of these problems share the exact same background "Engine". If you learn the pattern, you get multiple scripts for the price of one!

Here is your **3-Day AI Lab Preparation Strategy**, organized by difficulty and complexity, including time estimates and specific things to practice.

***

## 📅 Day 1: Search Fundamentals & Heuristics
*Total Time: ~5.5 Hours*
*Your goal for today is to understand how AI "looks around" for answers. Everything else builds on these State Space Search concepts.*

### 1. Missionaries & Cannibals (BFS & DFS) `[EASY]` - ⏳ 2 Hours
*   **Files:** `missionariescannibalsbfs.py`, `missionariescannibalsdfs.py`, `missionarybfs.py`
*   **Why start here?** It introduces you to the core concept of all classical AI: *State Space Search*. You will learn how to maintain paths dynamically.
*   **What to memorize:** The only code difference between the two is `queue.pop(0)` (BFS) vs `stack.pop()` (DFS).
*   **Things to practice:** Focus heavily on the `get_legal_moves()` function. Practice writing out the logic that ensures cannibals never outnumber missionaries on either side of the river. 

### 2. TSP Hill Climbing `[EASY]` - ⏳ 1 Hour
*   **Files:** `tsphillclimbing.py`
*   **Why?** It teaches Local Search. Instead of keeping a giant queue of alternative timelines (like BFS), you only look at your immediate neighbors.
*   **What to memorize:** The swap logic. How to swap two items in an array to create a "neighbor," and the condition to stop searching.
*   **Things to practice:** Try deliberately modifying the swap mechanism. Practice explaining its main weakness: getting stuck in a "Local Maximum."

### 3. A* Water Jug Problem `[DIFFICULT]` - ⏳ 2.5 Hours
*   **Files:** `astarwaterjug.py`
*   **Why?** Now that you understand basic BFS, A* is just BFS but with a "Smart GPS" priority queue (`heapq`).
*   **What to memorize:** The magic formula `f = g + h`. Remember what `g` (steps taken so far) and `h` (the heuristic guess of distance remaining) represent.
*   **Things to practice:** Practice writing a simple custom heuristic function. Manually write code using Python's `heapq` module (`heappush`, `heappop`) as this often trips up students.

***

## 📅 Day 2: Constraint Satisfaction & Logic
*Total Time: ~7 Hours*
*Your goal today is deductions. These don't use typical queues; they are about mathematical rules, variable satisfaction, and IF-THEN logic.*

### 4. Constraint Satisfaction Clones (Map & Sudoku) `[MODERATE]` - ⏳ 2 Hours
*   **Files:** `map.py`, `sudoko.py`
*   **Why?** Both are exactly the same concept: Assign a variable without breaking the rules (neighbors can't share colors / rows can't share numbers).
*   **What to memorize:** For Sudoku, the math to find a 3x3 subgrid: `(row // 3) * 3`.
*   **Things to practice:** Practice writing the "isValid()" checking function for both. That is the only hard part; the rest is a simple looping loop.

### 5. Cryptarithmetic `[MODERATE]` - ⏳ 1.5 Hours
*   **Files:** `cryptarithmetic.py`
*   **Why?** A step up in constraint combinations (SEND + MORE = MONEY). 
*   **What to memorize:** The recursive backtracking concept assigning unique digits to letters.
*   **Things to practice:** Focus on how the algorithm checks for leading zeroes and mathematically evaluates the word sum once digits are assigned.

### 6. Logic & Rule Brain Break `[MODERATE]` - ⏳ 3.5 Hours
*   **Files:** `bayesiannetwork.py` (*1 Hr*), `firstorderlogic.py` (*1 Hr*), `wumpuslogic.py` (*1.5 Hr*)
*   **Why?** This block shifts to pure probability and logic rules.
*   **What to memorize:**
    *   *Bayesian:* The Chain Rule (multiplying probabilities together).
    *   *First-Order Logic:* The loop comparing known facts against universal rules to append new facts.
    *   *Wumpus:* The concept of Process of Elimination using Python `Sets`.
*   **Things to practice:** For Bayesian, practice looking up conditional values in a nested dictionary. For Wumpus, practice using `intersection()` and `difference()` methods on Sets to deduce safe squares.

***

## 📅 Day 3: Planning, Games, & Advanced Recursion
*Total Time: ~7.5 Hours*
*Your final day covers the most complex scripts involving detailed game trees and deep recursion logic.*

### 7. The Planning Clones `[MODERATE]` - ⏳ 2 Hours
*   **Files:** `blocksworldplanning.py`, `monkeybananaplanning.py`
*   **Why?** These scripts actually use the exact same Breadth-First Search (BFS) engine you already learned in Day 1!
*   **What to memorize:** Don't memorize the queue logic. Focus strictly on defining the **Preconditions** and **Effects** inside `get_possible_moves()`.
*   **Things to practice:** Practice writing out states. E.g., for Monkey, practice tracking states like `height == floor` vs `height == box`.

### 8. Eight Queens Backtracking `[DIFFICULT]` - ⏳ 2.5 Hours
*   **Files:** `eightqueensbacktracking.py`
*   **Why it's hard:** Deep recursion. It drops a queen, calls itself, and if it fails, reverses backward.
*   **What to memorize:** The diagonal math trick: `abs(row1 - row2) == abs(col1 - col2)`.
*   **Things to practice:** The "Pencil and Eraser" concept. Practice writing the loop where you place a queen (Pencil), call the function, and if it returns `False`, remove the queen (Eraser).

### 9. Tic-Tac-Toe Alpha-Beta Pruning `[DIFFICULT]` - ⏳ 3 Hours
*   **Files:** `tictactoealphabeta.py`
*   **Why it's hard:** The Minimax algorithm travels all the way to the end of the game tree.
*   **What to memorize:** You don't need to perfectly memorize the whole thing. Focus heavily on the **Pruning** logic! Memorize the break condition: `if beta <= alpha: break`.
*   **Things to practice:** Manually draw a game tree on paper and trace the `alpha` and `beta` variables being passed up and down exactly once. This is guaranteed to click it permanently in your brain.

***

### 🎯 Final Review Tips (Night Before Exam):
1.  **Don't memorize syntax, memorize the Analogy:** If you forget how to write a Python Heap Queue for A*, write pseudo-code explaining the "Smart GPS" concept. You'll get partial or full credit.
2.  **Focus on the "Helper Functions":** In all search/planning scripts, the actual searching loop is identical. The only thing that changes is the `get_legal_moves()`. Direct your review there.
3.  **Trace it on paper:** Your pen is your best friend for Eight Queens and Tic-Tac-Toe. Trace them out!
