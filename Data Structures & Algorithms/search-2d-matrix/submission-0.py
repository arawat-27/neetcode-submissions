class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #check every row
        # use binary search to check if the elements in the row are bigger or smaller than the target. if it's bigger move to the next row
        ROWS, COLS = len(matrix), len(matrix[0])

        t = 0
        b = ROWS - 1
        while t <= b:
            row = (t + b) // 2
            if target > matrix[row][-1]:
                t = row + 1
            elif target < matrix[row][0]:
                b = row - 1
            else:
                break
        
        if not (t <= b):
            return False
        row = (t + b) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
              



                
        