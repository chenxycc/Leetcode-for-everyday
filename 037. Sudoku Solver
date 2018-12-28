class Solution(object):
    def isValue(self,board,x,y):
        #检查填入的坐标是否与行中已有元素相等
        #列符合
        for i in range(9):
            if i != x and board[i][y] == board[x][y]:
                return False
        #检查行是否符合
        for j in range(9):
            if j != y and board[x][j] == board[x][y]:
                return False
        
        #检查每个正方形是否符合
        #以下代码教会了我们如何遍历3*3方块
        m = 3*(x // 3);n = 3*(y // 3)
        for i in range(3):
            for j in range(3):
                if (i + m != x or j + n != y) and board[i + m][j + n] == board[x][y]:
                    return False
        return True
    def dfs(self,board):
        #遍历每一个坐标
        for i in range(9):
            for j in range(9):
                #找board里的需要填入的位置
                if board[i][j] == '.':
                    #从可选之间选一个
                    for k in '123456789':
                        board[i][j] = k
                        #在if的时候调用递归
                        #如果这个递归可以返回true并且当前填入的数字也没毛病
                        #则证明我们解完了数独
                        if self.isValue(board,i,j) and self.dfs(board):
                            return True
                        #到这个位置说明填入的数不太行，所以把它先空着。
                        board[i][j] = '.'
                    #进行完当前可选的所有数字都不行，说明上一次决策有问题，返回false
                
                    return False
        #所有'.'都填满，并且没毛病，返回true
        return True
        
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.dfs(board)
