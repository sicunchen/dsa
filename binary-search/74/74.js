// solution 2
const searchMatrix2 = function (matrix, target) {
  let row = 0;
  let col = matrix[0].length - 1;
  while (col >= 0 && row < matrix.length) {
    if (matrix[row][col] == target) {
      return true;
    } else if (matrix[row][col] < target) {
      row++;
    } else {
      col--;
    }
  }

  return false;
};

//solution 3
const searchMatrix3 = function (matrix, target) {
  const m = matrix[0].length;
  const n = matrix.length;
  let start = 0;
  let end = m * n - 1;
  while (start + 1 < end) {
    let mid = Math.floor((start + end) / 2);
    const value = matrix[Math.floor(mid / m)][mid % m];
    if (value == target) {
      return true;
    } else if (value < target) {
      start = mid;
    } else {
      end = mid;
    }
  }

  if (target == matrix[Math.floor(start / m)][start % m]) return true;
  if (target == matrix[Math.floor(end / m)][end % m]) return true;
  return false;
};
