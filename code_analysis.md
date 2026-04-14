# AI Algorithms Analysis & Learning Guide

This document breaks down the code logic and complexity for both `sudoko.py` and `map.py`. It is designed to help you segregate the logic into digestible parts so you can easily learn and understand how they work.

---

## 🌟 The Grand Similarity: Concept & Logic

Before diving into the specifics of each script, it is highly beneficial to understand that **both of these scripts are fundamentally identical in their core concept and logic**. 

Both scripts are solving **Constraint Satisfaction Problems (CSPs)** using the **Backtracking algorithm**. If you understand the structure of one, you automatically understand the structure of the other. 

Here is how their logic directly mirrors each other:

| Logical Component | Sudoku Solver (`sudoko.py`) | Map Coloring (`map.py`) | What it means |
| :--- | :--- | :--- | :--- |
| **The Target (Variables)** | Empty cells (`0`) on the 9x9 board. | Uncolored regions on the map. | The items we are trying to find an answer for. |
| **The Choices (Domain)** | Numbers `1` through `9`. | Available colors (`Red`, `Green`, `Blue`). | The pool of possible options we can assign to the Target. |
| **Constraint Checker** | `isvalid(board, row, col, num)`<br>Checks row, column, and 3x3 grid. | `isvalid(region, color, assignment)`<br>Checks neighboring regions in the graph. | The rulebook. It returns `False` if assigning a Choice to a Target breaks the rules. |
| **Making a Guess** | `board[row][col] = num` | `assignment[region] = color` | Temporarily committing to a choice assuming it is correct. |
| **Diving Deeper** | `if solvesudoku(board):` | `result = backtrack(assignment)` | Recursively calling the function to move to the *next* Target variable. |
| **The Backtrack (Undo)** | `board[row][col] = 0` | `del assignment[region]` | If a guess leads to a dead-end later on, we "undo" our guess and try the next Choice. |
| **Base Case (Success)** | No empty cells remaining. | Dictionary size == Total regions. | We have correctly assigned a choice to every single target. |

By recognizing these parallels, you don't have to learn two separate algorithms—you only have to learn the **Backtracking Template**, and then see how it applies to grids (Sudoku) vs. graphs (Maps).

---

## 1. Sudoku Solver (`sudoko.py`)

### Core Concept
The Sudoku solver uses Backtracking to try filling the board cell by cell, undoing mistakes as they are detected.

### Code Logic Breakdown

**A. Constraint Checking (`isvalid` function)**
Before placing any number, we must ensure it doesn't violate Sudoku rules:
1. **Row Check:** Iterates through the current row to see if the number already exists.
2. **Column Check:** Iterates through the current column to see if the number already exists.
3. **Subgrid (3x3) Check:** Calculates the top-left corner of the current 3x3 block using modulo (`%`) and checks all 9 cells inside it.

**B. Recursive Search (`solvesudoku` function)**
1. **Find Empty Cell:** It loops through every row and column until it finds an empty cell (`0`).
2. **Guessing:** It tries placing numbers `1` through `9`.
3. **Recursive Step:** If `isvalid` returns `True`, it places the number and immediately calls *itself* to proceed to the next cell.
4. **The Backtrack:** If a later cell returns `False`, it resets the current cell back to `0` and tries the next number.

### Complexity
* **Time Complexity:** **O(9^(n*m))** in the worst case, where `n*m` is the number of empty cells (max 81). The `isvalid` check heavily prunes the search tree, heavily optimizing this in practice.
* **Space Complexity:** **O(1)** auxiliary space. Since the board size is fixed at 9x9, the maximum depth of the recursive call stack is 81.

---

## 2. Map Coloring Problem (`map.py`)

### Core Concept
This script also uses Backtracking to solve a CSP. The goal is to color regions on a graph/map so that no two touching (adjacent) regions have the same color. 

### Code Logic Breakdown

**A. Setup & Graph Representation**
* `neighbors`: An adjacency list representing the graph. For example, `'A': ['B', 'C']` means region A touches B and C.

**B. Constraint Checking (`isvalid` function)**
* It loops through all neighboring regions of the current `region`.
* If a neighbor is already tracked in our `assignment` dictionary AND it shares the color we want to use, it returns `False`.

**C. Recursive Assignment (`backtrack` function)**
1. **Base Case:** If `len(assignment) == len(regions)`, the map is fully colored.
2. **Select Variable:** Find an unassigned region (loops through `regions` until it finds one not in `assignment`).
3. **Try Values:** It tries iterating through all available `colors`.
4. **Recursive Step:** If the color is valid, add it to the dictionary, and recursively call `backtrack`.
5. **The Backtrack:** If a downstream recursive call hits a dead end (`None`), it deletes the color from the dictionary using `del assignment[region]` and tries the next color.

### Complexity
* **Time Complexity:** **O(C^V)**, where `C` is the number of colors and `V` is the number of vertices (regions). At each region, it branches out `C` times.
* **Space Complexity:** **O(V)**. The recursion depth and the variables required for the `assignment` tracking scale linearly with the number of regions.
