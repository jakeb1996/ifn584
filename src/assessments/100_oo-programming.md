---
name: "IFN584 Assignment 1 - Object-oriented programming"
---

[TOC]

## Overview

In this task you will complete an object-oriented programming exercise based on a simple design in order to reinforce your object-oriented programming knowledge and prepare you for the larger design-and-implementation task in the next assignment.

The submission must be your own original work. Plagiarising the work of others is strictly prohibited at QUT, and submissions will be checked for code plagiarism. Furthermore, using generative AI tools like ChatGPT, including programming/coding assistants like CoPilot, **is forbidden for all assessment tasks in IFN584**. Any such use will be considered an act of academic misconduct.

This assignment is eligible for the 48-hour late submission period and assignment extensions.

- Weight: **25%**
- Individual/Group: **Individual**
- Due: **Friday 29 August (Week 6)**

## Introduction

Connect Four is a classic strategy game first released by the Milton Bradley Company in February 1974. It features a vertical grid into which two players take turns dropping coloured discs. Each disc falls to the lowest available space within a column. The objective is simple: be the first to align four discs in a row: vertically, horizontally, or diagonally.

The standard Connect Four grid consists of six rows and seven columns, totalling 42 cells. Each player is typically given 21 discs, enough to fill half the grid if the game reaches completion without a winner.

While the traditional format is widely recognised, many variations exist. Some versions use larger grids, one requires players to fill the lowest unfilled row before moving upward, and some feature special discs with unique abilities. These add layers of complexity and strategy. We have designed a renamed edition of the game, "LineUp", based on some of these alternatives. Your task is to implement LineUp.

## Task description

In this assignment, your task is to develop LineUp as a **C# console application on .NET 8** and have a text-based command-line interface (e.g. using either ASCII or Unicode) for playing from a terminal.

The program supports **two different modes of play**, including:

- Human vs Human
- Human vs Computer

With human players, the program checks the validity of moves as they are entered. With computer players, the program makes a move that immediately win the game; otherwise, if no immediate winning move is available, the computer player randomly selects a valid move.

A game can be **saved and restored** from any state of play, which is stored in a save file. Upon loading a save file, the game resumes from the exact position it was saved, preserving game modes (HvH or HvC) as well.

The program should provide a simple in-game **help menu** system to guide users with the available commands. Additionally, it can provide some examples of commands that may not be immediately apparent to users.

## Gameplay of LineUp

Your program begins by presenting the user with an option to load an existing game from a save or initiate a fresh game. Upon selecting a new game, the player is prompted to select the desired game modes as well as the size of the grid: number of rows and columns.

For each player's turn, the program displays the current grid and prompts the player to make a move, save the game, or view the help menu. When the player chooses to make a move, their turn ends, and the other player's turn begins. If the other player is a computer player, they make a move immediately without prompting. If the player chooses to save the game, the current gameplay is saved, and the game continues. If the player chooses to view the help menu, the available commands and possible examples are displayed.

The two players take turns to make moves until the game is over. The game ends when one of the players wins the game or when the grid is completely filled and no more move is possible; in this case, the game ends in a tie. When a game finishes, the program displays the final grid and reports the results before exiting.

Your program should also be able to handle invalid inputs by prompting the player to re-enter until a valid input is provided.

### The grid

The game board in LineUp is displayed using a grid format where each column is three whitespace characters wide, and column borders are drawn using the pipe character `|`. This layout ensures consistent spacing and visual clarity in the console.

Below is an example of a blank $6 \times 7$ grid, which is the default size:

```
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
```


The left-most column is referred to as the first column, followed by the second column, third column, and so on, moving rightward.

The bottom-most row is referred to as the first row, because discs follow gravity and land in this row first when dropped into an empty column.
    
Rows are numbered bottom to top, while columns are numbered left to right.

### Ordinary discs

In the standard version of Connect Four, each player is equipped with a set of ordinary discs. These discs are the foundation of gameplay and follow the basic rules:

   - **Gravity-based placement:** When dropped into a column, an ordinary disc falls to the lowest available space.

   - **Winning condition:** Players aim to align four ordinary discs in a row: vertically, horizontally, or diagonally.

   - **No special effects:** Ordinary discs do not interact with other discs beyond forming connections. They cannot destroy, move, or influence other discs.
    
   - **Count toward victory:** Every ordinary disc placed on the grid contributes toward achieving a win.

These discs form the backbone of the game, offering a simple yet strategic experience.

LineUp has the same ordinary disc.

### Special discs

Unlike Connect Four, LineUp features discs that have special abilities.

These discs must be identifiable in the grid when played. 

- **Boring disc:** When played, this disc bores (*to make a hole*) all existing discs from the selected column, returning them to their respective players' hands. The boring disc itself remains permanently at the bottom of the column and is considered an Ordinary Disc after the round has ended. This disc can count toward a victory.

- **Magnetic disc:** When played, this disc exerts a vertical magnetic force within the column it is dropped into. It lifts the nearest ordinary disc belonging to the same player one position upward. That makes this most useful when dropped on top of an ordinacy disc of the opposition. The Magnetic Disc can affect only one disc, and its effect is triggered once upon placement. After activation, it becomes an Ordinary Disc and can contribute toward a winning alignment.

- **Exploding disc:** This disc is destructive. Upon landing, it detonates, destroying any discs it touches (including on the diagonal), no matter their owner. The explosion clears those positions. The destroyed discs are not returned to their respective players' hands. As the disc itself is destroyed upon landing, it cannot count toward a victory.

Each player is allotted two of each type of special disc, which they may use in place of ordinary discs during gameplay.

Given that each special disc alters the state of the grid, the game should display up to three distinct frames to visually communicate the change:

   1. Initial placement: The disc lands in its designated position, following the standard gravity-based drop.
    
   1. Effect activation: The disc triggers its unique ability, modifying the grid accordingly (e.g., pulling, destroying, or displacing other discs).
    
   1. Final grid state, only relevant to the Exploding Disc: The grid reflects the outcome of the explosion. The exploded disc itself and its neighbouring discs must be removed after detonation and leave behind an altered grid.

### Grid size

In the setup of the game, players can customise the grid size to suit different play styles. A custom grid cannot be smaller than the default ($ 6 \times 7 $). The grid can be a square but can never have more rows than columns.

Each player receives a number of discs equal to half the total grid cells, with two of each special disc type included in that total. The remaining discs are ordinary, used for standard gameplay. For example, on a $ 6 \times 7 $ grid (42 cells), each player gets 21 discs: they will have 6 special discs and 15 ordinary ones.

For grids that are not the standard size, the number of discs required to align in order to win is calculated as:

$$
\left\lfloor \text{NUM\_ROWS} \times \text{NUM\_COLS} \times 0.1 \right\rfloor
$$

## Disc Representation in Console Grid

In the C# console version of *LineUp*, each disc type is represented by a distinct character to ensure clarity and readability on screen. 

Special discs must also be easily identifiable in the grid. Each player is allotted two of each type, and their representations are as follows:

| Player | Disc Type      | Character |
| ------ | -------------- | --------- |
| 1      | Ordinary       | `@`       |
| 2      | Ordinary       | `#`       |
| 1      | Boring Disc    | `B`       |
| 2      | Boring Disc    | `b`       |
| 1      | Magnetic Disc  | `M`       |
| 2      | Magnetic Disc  | `m`       |
| 1      | Exploding Disc | `E`       |
| 2      | Exploding Disc | `e`       |

Uppercase letters are used for Player 1's special discs and lowercase for Player 2's, making it easy to distinguish both the disc type and the player who placed it. 

## Example grids

### Basic game play

Suppose this game is played only with Ordinary Discs.

Given the following order of plays

- P1 played in column 4 (landing in row 1)
- P2 played in column 5 (landing in row 1)
- P1 played in column 3 (landing in row 1)
- P2 played in column 6 (landing in row 1)
- P1 played in column 2 (landing in row 1)
- P2 played in column 5 (landing in row 2)
- P1 played in column 4 (landing in row 2)
- P2 played in column 5 (landing in row 3)
- P1 played in column 4 (landing in row 3)
- P2 played in column 5 (landing in row 4)

... the grid appears as:

```
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   | # |   |   |
|   |   |   | @ | # |   |   |
|   |   |   | @ | # |   |   |
|   | @ | @ | @ | # | # |   |
```

The game ends because P2 has lined up four discs in the fifth column.


### Using a Boring Disc 

Suppose the grid prior to P2 playing a Boring Disc looked like this:

```
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   | @ | # |   |   |
|   |   |   | @ | # | @ |   |
|   | @ | @ | @ | # | # | # |
```

P2 plays the Boring Disc into the forth column:

```
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   | b |   |   |   |
|   |   |   | @ | # |   |   |
|   |   |   | @ | # | @ |   |
|   | @ | @ | @ | # | # | # |
```

The Bording Disc removes all discs below it:

```
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   | # |   |   |
|   |   |   |   | # | @ |   |
|   | @ | @ | b | # | # | # |
```

The game ends because P2 has lined up four discs in the first row.

### Using a Magnetic Disc

Suppose the grid prior to P1 playing a Magnetic Disc (m) looked like this:

```
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   | @ |   |   |   |   |   |
| # | # | # | @ | # | @ | @ |
| @ | # | @ | # | @ | # | @ |
```

P2 plays a Magnetic Disc (m) into the forth column:

```
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   | @ |   | m |   |   |   |
| # | # | # | @ | # | @ | @ |
| @ | # | @ | # | @ | # | @ |
```

The Magnetic Disc lifts the Ordinary Disc of P2 from the first row to the second row, and the Ordinary Disc of P1 falls from the second row to the first row:

```
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   | @ |   | m |   |   |   |
| # | # | # | # | # | @ | @ |
| @ | # | @ | @ | @ | # | @ |
```

The game ends because P2 has lined up four (or more) discs in the second row.

### Using an Exploding Disc

Suppose the grid before Player 2 plays an Exploding Disc (e) in the third column looks like this:

```
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   | # |   |   | @ |   |   |
|   | @ |   |   | # |   |   |
|   | @ |   |   | # |   |   |
|   | @ | @ |   | # |   |   |
```

Player 2 plays an Exploding Disc (e) into the third column. It lands in the second row:

```
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   | # |   |   | @ |   |   |
|   | @ |   |   | # |   |   |
|   | @ | e |   | # |   |   |
|   | @ | @ |   | # |   |   |
```

The Exploding Disc destroys:

   - Itself (e)
   - The adjacent discs:
      - First row, second and third column
      - Second row, second column
      - Third row, second column

After the explosion, the grid is updated. Remaining discs fall to fill the gaps:

```
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   | @ |   |   |
|   |   |   |   | # |   |   |
|   |   |   |   | # |   |   |
|   | # |   |   | # |   |   |
```

There is not yet a winner. The game continues.

## Testing Mode Specification

You must implement a testing mode that accepts a single line of input describing a sequence of plays.

- Player 1 (P1) always starts the game.
- Players alternate turns.
- Each play consists of:
  - A disc type (case-insensitive):  
    - `O`: Ordinary Disc  
    - `E`: Exploding Disc  
    - `M`: Magnetic Disc  
    - `B`: Boring Disc
  - A column number indicating where the disc is dropped.
- Plays are separated by commas.

Suppose the input were:

```
O4,O5,O3,O6,O2,O5,O4,O5,E4,M5,B4
```

Then, this is interpreted as:

```
1. P1 — Ordinary Disc — Column 4  
2. P2 — Ordinary Disc — Column 5  
3. P1 — Ordinary Disc — Column 3  
4. P2 — Ordinary Disc — Column 6  
5. P1 — Ordinary Disc — Column 2  
6. P2 — Ordinary Disc — Column 5  
7. P1 — Ordinary Disc — Column 4  
8. P2 — Ordinary Disc — Column 5  
9. P1 — Exploding Disc — Column 4  
10. P2 — Magnetic Disc — Column 5  
11. P1 — Boring Disc — Column 4
```

This testing mode will be used to evaluate your game implementation. Ensure that it correctly interprets the input sequence, applies the appropriate disc types, and maintains accurate turn order and game logic throughout.

## Marking Criteria (25 points total)

Here is a guide to how your response to this assignment will be marked:

| Grade                | Feature Completion                                        | Code Quality & Usability                                                              |
| -------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **High Distinction** | All features fully implemented and functional             | Clean, well-structured, fully commented code. Intuitive UI, bug-free, handles errors. |
| **Distinction**      | Almost all features implemented and functional            | Mostly clean code. Minor UI or input issues. Few bugs.                                |
| **Credit**           | Some features implemented and functional                  | Readable code with some structure. Basic UI. Some bugs or input issues.               |
| **Pass**             | The basic features are implemented and functional         | Functional but messy code. Minimal UI. Frequent bugs or crashes.                      |
| **Below Pass**       | The basics are not functional or there are major problems | Incomplete, buggy, or unreadable code. UI is confusing or non-functional.             |

We will be looking for:

- A functioning test mode (without this, marking your game may be very difficult).
- The game with grid size $6 \times 7$ and only ordinary discs can be successfully played from start to finish. (5 points)
- The game with arbitrary grid size $n \times m$ can be successfully played from start to finish. (5 points)
- The game with special discs can be successfully played from start to finish. (5 points)
- The game can be successfully saved and restored from any state of play; it can resume from the exact position it was saved. (5 points)
- Usability and code quality are excellent. The user interface and commands are simple and clear, with a helpful menu system. The program is bug-free and can handle invalid inputs. The source code is well-structured and commented for readability. (5 points, subject to the completion of other task requirements)

## Submission

The submission link for this assignment will be open on the IFN584 Canvas website. To submit, you must create **a ZIP file** that contains all your C# project files. Specifically, zip your working implementation, including the complete C# project source code for .NET 8, and upload this ZIP file to the IFN584 Canvas website.

The submitted project files will be compiled and executed on QUT lab computers with .NET 8. **You must make sure that your submitted code can be compiled and run properly** under this environment.

Uncompilable or inexecutable source code cannot be marked and will receive a zero. To confirm the version of .NET on your computer, simply open a terminal and execute the following command:

```shell
dotnet --version
```

To check that your project code can be compiled and executed on .NET 8, open a terminal in the folder containing the project file (`.csproj`) and run the following commands:

```shell
dotnet clean
dotnet run
```
