/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function(grid) {
  let fresh = 0;
  let rottenOranges = [];
  const rowCount = grid.length;
  const colCount = grid[0].length;
  for (let i = 0; i < rowCount; i++) {
    for (let j = 0; j < colCount; j++) {
      if (grid[i][j] == 1) {
        fresh++;
      } else if (grid[i][j] == 2) {
        rottenOranges.push([j, i]);
      }
    }
  }
  let mins = 0;
  while (rottenOranges.length !== 0 && fresh !== 0) {
    const size = rottenOranges.length;
    for (let i = 0; i < size; i++) {
      let [x, y] = rottenOranges.shift();
      if (x - 1 >= 0 && grid[y][x - 1] == 1) {
        grid[y][x - 1] = 2;
        rottenOranges.push([x - 1, y]);
        fresh--;
      }

      if (x + 1 < colCount && grid[y][x + 1] == 1) {
        grid[y][x + 1] = 2;
        rottenOranges.push([x + 1, y]);
        fresh--;
      }
      if (y + 1 < rowCount && grid[y + 1][x] == 1) {
        grid[y + 1][x] = 2;
        rottenOranges.push([x, y + 1]);
        fresh--;
      }
      if (y - 1 >= 0 && grid[y - 1][x] == 1) {
        grid[y - 1][x] = 2;
        rottenOranges.push([x, y - 1]);
        fresh--;
      }
    }
    mins++;
  }
  return fresh === 0 ? mins : -1;
};
