class Solution:
    def exist(self, board, word):
        for r in range(len(board)):
            for c in range(len(board[0])):
                print(board[r][c])
                
                if word[0] == board[r][c]:
                    row = r
                    col = c
                    pointer = 0
                    
                    if pointer < len(word)-1:
                        while(word[pointer+1]== board[row+1][col] or 
                            word[pointer+1]== board[row][col+1] or 
                            word[pointer+1]== board[row-1][col] or 
                            word[pointer+1]== board[row][col-1]):
                            
                            if word[pointer+1]== board[row+1][col]:
                                row +=1
                                
                            if word[pointer+1]== board[row][col+1]:
                                col +=1
                                
                            if word[pointer+1]== board[row-1][col]:
                                row -=1
                                
                            if word[pointer+1]== board[row][col-1]:
                                col -=1
                            if(pointer < len(word)-1):
                                pointer += 1
                            print(pointer)

                    else:
                        return True
        
        
        
        
        
        
        



board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"


obj = Solution()
print(obj.exist(board,word))
