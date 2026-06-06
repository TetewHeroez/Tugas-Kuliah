export interface SudokuPuzzle {
  solution: number[][];
  given: boolean[][];
}

export const GRID_SIZE = 9;
export const BLOCK_SIZE = 3;

export const mainPuzzle: SudokuPuzzle = {
  solution: [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [9, 1, 2, 3, 4, 5, 6, 7, 8],
  ],
  given: [
    [true, true, false, true, true, false, true, false, true],
    [true, false, true, true, false, true, false, true, true],
    [false, true, true, false, true, true, true, true, false],
    [true, true, false, true, false, true, true, false, true],
    [true, false, true, false, true, false, true, false, true],
    [false, true, true, true, false, true, false, true, true],
    [true, false, true, true, true, false, true, true, false],
    [true, true, false, false, true, true, true, false, true],
    [false, true, true, true, false, true, false, true, true],
  ],
};

export function blockOf(row: number, col: number): number {
  const br = Math.floor(row / BLOCK_SIZE);
  const bc = Math.floor(col / BLOCK_SIZE);
  return br * BLOCK_SIZE + bc;
}

export function getConflicts(
  grid: (number | null)[][],
  row: number,
  col: number,
  num: number
): { row: boolean; col: boolean; block: boolean } {
  let rowConflict = false;
  let colConflict = false;
  let blockConflict = false;

  for (let c = 0; c < GRID_SIZE; c++) {
    if (c !== col && grid[row][c] === num) {
      rowConflict = true;
      break;
    }
  }

  for (let r = 0; r < GRID_SIZE; r++) {
    if (r !== row && grid[r][col] === num) {
      colConflict = true;
      break;
    }
  }

  const blockRowStart = Math.floor(row / BLOCK_SIZE) * BLOCK_SIZE;
  const blockColStart = Math.floor(col / BLOCK_SIZE) * BLOCK_SIZE;
  outer: for (let r = blockRowStart; r < blockRowStart + BLOCK_SIZE; r++) {
    for (let c = blockColStart; c < blockColStart + BLOCK_SIZE; c++) {
      if ((r !== row || c !== col) && grid[r][c] === num) {
        blockConflict = true;
        break outer;
      }
    }
  }

  return { row: rowConflict, col: colConflict, block: blockConflict };
}

export function cellHasConflict(
  grid: (number | null)[][],
  row: number,
  col: number
): boolean {
  const val = grid[row][col];
  if (val === null) return false;

  const conflicts = getConflicts(grid, row, col, val);
  return conflicts.row || conflicts.col || conflicts.block;
}

export function isGridComplete(grid: (number | null)[][]): boolean {
  for (let r = 0; r < GRID_SIZE; r++) {
    for (let c = 0; c < GRID_SIZE; c++) {
      if (grid[r][c] === null || cellHasConflict(grid, r, c)) return false;
    }
  }

  return true;
}

export function initializeGrid(puzzle: SudokuPuzzle): (number | null)[][] {
  return puzzle.solution.map((row, r) =>
    row.map((val, c) => (puzzle.given[r][c] ? val : null))
  );
}
