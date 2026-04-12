#  1-Day AI Lab Survival Strategy

Since you only have **one day** to prepare, we need a high-efficiency battle plan! 

The good news is that many of these problems share the exact same background "Engine" (for example, the Planner for Blocks World, Monkey & Bananas, and Missionaries BFS are almost identical block-for-block!). If you learn the pattern, you get 3 scripts for the price of 1!

Here is your **1-Day AI Lab Survival Strategy**, categorized by difficulty and ordered logically so the concepts build on each other.

***

##  Block 1: The Search Fundamentals (Start Here!)
*Start your morning here. These teach you how AI "looks around" for answers. Everything else builds on this.*

### 1. Missionaries & Cannibals (BFS & DFS) `[EASY]`
*   **Why start here?** It introduces you to the core concept of all classical AI: *State Space Search*. 
*   **What to memorize:** The only code difference between the two is `queue.pop(0)` (BFS) vs `stack.pop()` (DFS). Memorize how the `get_legal_moves()` function works to simulate future timelines safely.

### 2. TSP Hill Climbing `[EASY]`
*   **Why?** It teaches Local Search. Instead of keeping a giant queue of alternative timelines (like BFS), you only look at your immediate neighbors.
*   **What to memorize:** The swap logic. How to swap two items in an array to create a "neighbor," and how the `while True` loop stops if no neighbor is better than your current state.

### 3. A* Water Jug Problem `[DIFFICULT]`
*   **Why?** Now that you understand basic BFS, A* is just BFS but with a "Smart GPS" priority queue (`heapq`).
*   **What to memorize:** The magic formula `f = g + h`. Remember what `g` (steps taken so far) and `h` (the heuristic guess of distance remaining) actually represent in code.

***

##  Block 2: Logic & Probabilities (The Brain Break)
*Do this midday. These don't use queues or stacks making them a nice mental break. They are purely mathematical and logical IF-THEN deductions.*

### 4. Bayesian Network `[EASY]`
*   **Why?** This is the easiest code in the folder. It's just Python dictionary lookups and basic multiplication.
*   **What to memorize:** The Chain Rule. Just remember that you lookup the probability for each event, and multiply all those individual `.get_chance()` variables together at the very end.

### 5. First-Order Logic (Forward Chaining) `[MODERATE]`
*   **Why?** Introduces the concept of a "Knowledge Base" for AI.
*   **What to memorize:** The giant `while True` loop that compares known **facts** against the universal **IF-THEN rules** to append new deduced facts. 

### 6. Wumpus World Logic `[MODERATE]`
*   **Why?** Applies propositional logic to a physical grid scenario.
*   **What to memorize:** The concept of Process of Elimination using Python `Sets`. Remember that smelling a stench means finding the *Intersection* of possibilities, and feeling NO stench means *Removing* possibilities.

***

##  Block 3: The Planning Clones (2-for-1 Special)
*Once you reach here, you are actually revisiting Block 1. Both of these scripts use the exact same Breadth-First Search (BFS) engine you already learned in the Missionaries problem!*

### 7. Blocks World Planning `[MODERATE]`
### 8. Monkey and Banana Planning `[MODERATE]`
*   **The Strategy:** Don't try to memorize the `planner()` function here—it's just a standard BFS queue loop. 
*   **What to actually memorize:** Focus entirely on the **Preconditions** and **Effects** inside `get_possible_moves()`. 
    *   For Blocks World, remember it uses `.pop()` to simulate robotic arm lifting.
    *   For Monkey, remember it checks dictionary states like `height == floor`.

***

##  Block 4: The Final Bosses (Recursion)
*Save these for last. They are the hardest to read because they use "Recursion" (functions calling themselves over and over), which can mess with your head.*

### 9. Eight Queens Backtracking `[DIFFICULT]`
*   **Why it's hard:** It drops a queen, calls itself to drop the next queen, and if it fails, it reverses backward up the chain.
*   **What to memorize:** The "Pencil and Eraser" concept. Pay attention to the part where the array assigns a column (Pencil), calls `solve_queens()`, and if it returns False, overwrites the array with `-1` (Eraser). Also, memorize the diagonal math trick: `abs(row1 - row2) == abs(col1 - col2)`.

### 10. Tic-Tac-Toe Alpha Beta Pruning `[DIFFICULT]`
*   **Why it's hard:** The Minimax algorithm travels all the way to the end of the game tree, passing variables up and down.
*   **What to memorize:** You don't need to perfectly memorize the whole thing. Focus heavily on the **Pruning** logic!
    *   Memorize exactly what `Alpha` (Max's guaranteed score) and `Beta` (Min's guaranteed score) are. 
    *   Memorize the break condition: `if beta <= alpha: break`. If you can explain *why* that break statement is there on an exam, you will easily pass.

***

###  Extra Tips for Tomorrow's Exam:
1.  **Don't memorize syntax, memorize the Analogy:** If you forget how to write a Python Heap Queue for A*, don't panic. Write pseudo-code! If you can explain the "Wizard/Smart GPS" concept mathematically on paper, teachers will give you 90% of the marks.
2.  **Focus on the "Helper Functions":** In all the BFS/Planning scripts, the actual searching loop is identical. The only thing that changes is the `get_legal_moves()` function. Focus your study time on how legal moves are generated.
3.  **Trace it on paper:** For the difficult ones (8-Queens and Tic-Tac-Toe), take 15 minutes today to literally draw a grid on paper and manually trace what the code is doing exactly once. It will make the code click in your brain permanently!
