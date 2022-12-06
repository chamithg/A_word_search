class Solution:
    def exist(self, board, word):
        
        
        # find the height and width of the board
        height, width = len(board), len(board[0])
        
        # create a set to hold the position of match found
        # this prevent iterating over same box again
        path = set()
        
        def dfs(r,c,i):
            
            # if i reach the end of the word which means match found
            if i == len(word):
                return True
            if (r < 0 or c < 0 or 
                r>= height or 
                c >= width or 
                word[i] != board[r][c] or 
                (r,c) in path):
                return False
            path.add((r,c))
            res = (dfs(r+1,c,i+1 ) or
                   dfs(r,c+1,i+1 ) or
                   dfs(r-1,c,i+1 ) or
                   dfs(r,c-1,i+1 ))
            path.remove((r,c))
            return res

        
        for r in range(height):
            for c in range(width):
                if board[r][c] == word[0]:
                    if dfs(r,c,0): return True
                    
        return False
        
        
        
        



board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"


obj = Solution()
print(obj.exist(board,word))
