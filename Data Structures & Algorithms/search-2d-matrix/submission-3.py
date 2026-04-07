class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix) , len(matrix[0])

        # binary searc over rows to find the right one
        top, bottom = 0, rows - 1
        while top <= bottom:
            row = top + ((bottom - top) //  2) 

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        if not (top <= bottom):
            return False
        

        # binary search over targeted row to find the value
        l , r = 0, cols -1
        row = top + ((bottom - top) // 2)
        while l <= r:
            mid = l + ((r - l) // 2)

            if target < matrix[row][mid]:
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True
        
        return False