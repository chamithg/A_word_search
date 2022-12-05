class Solution:
    def exist(self, board, word):
        
        height, width = len(board), len(board[0])
        
        
        def run(row,col,pos,temp):
            print(temp, pos)
            if temp == word:
                return True
            
            if row < height-1 and word[pos+1]== board[row+1][col]:
                temp += board[row+1][col]
                run(row +1 ,col,pos +1,temp)
            elif col < width-1  and word[pos+1]== board[row][col+1]:
                temp += board[row][col+1]
                run(row ,col+1,pos +1,temp)
            elif row > 0 and word[pos+1]== board[row-1][col]:
                temp += board[row-1][col]
                run(row -1 ,col,pos +1,temp)
            elif col > 0 and word[pos+1]== board[row][col-1]:
                temp += board[row][col-1]
                run(row  ,col-1,pos +1,temp)                      
            
        
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if word[0] == board[r][c]:
                    run(r,c,0,board[r][c])

                    
            return False
        
        
        
        
        



board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"


obj = Solution()
print(obj.exist(board,word))
