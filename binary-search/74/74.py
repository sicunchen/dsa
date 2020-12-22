# https://leetcode.com/problems/search-a-2d-matrix/

"""
Solution 1: Perform binary search on each row independently. 
O(mlogn)
"""


class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        i = 0
        n = len(matrix)
        while i < n - 1:
            if self.binarySearch(matrix[i], target):
                return True
            else:
                if target < matrix[i + 1][0]:
                    return False
                else:
                    i += 1
        if self.binarySearch(matrix[i], target):
            return True
        else:
            return False

        row, col = 0, len(matrix[0]) - 1
        while col >= 0 and row < len(matrix):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False


"""
Solution 2: Solution 1 fails to take advantage of the fact that BOTH rows and columns are sorted.
Suppose we compare target with matrix[0][m-1]:
* if target = matrix[0][m-1], we've found the target
* if target > matrix[0][m-1], then target is greater than all elements in row 0 
* if target < martrix[0][m-1], then target is less than all elements in col m-1
In either case, we have a matrix with one row OR column less to search.
O(m+n)
"""


class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row, col = 0, len(matrix[0]) - 1
        while col >= 0 and row < len(matrix):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False


"""
Solution 3: Convert the matrix into a 1d array. Perform binary search on this array. Pay attention to 
the matrix coordinates transformation.
O(logmn) aka O(logm+logn)
"""


class Solution3:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix[0]), len(matrix)
        start, end = 0, m * n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            value = matrix[mid // m][mid % m]
            if value == target:
                return True
            elif value < target:
                start = mid
            else:
                end = mid

        if target == matrix[start // m][start % m]:
            return True
        if target == matrix[end // m][end % m]:
            return True
        return False
