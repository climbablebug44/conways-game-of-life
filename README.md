## A simple implementation of Conway's Game of Life using python's pygame module
## Rules: At each step in time, the following transitions occur:

- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

## using the rules and an initial seed, press enter to continue the game on its own. click on any square to turn it on manually, when the game is paused or when its live.

## Screen cartesian in pygame
```
(0,0)                      (0,+x)   
  --------------------------->
  |
  |
  |
  |
  |
(+y,0)
  v

```