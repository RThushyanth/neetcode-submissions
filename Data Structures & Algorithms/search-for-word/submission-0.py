class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        riindex = len(board)-1
        rjindex = len(board[0])-1


        def search(searchi,curri,currj,brd):

            if brd[curri][currj] == word[searchi]:
                temp = brd[curri][currj]
                brd[curri][currj] = 0
                if searchi == len(word)-1:
                    return "Present"

                if curri != 0:
                    if search(searchi+1,curri-1,currj,brd) != None:
                        return "Present"
                
                if curri != riindex:
                    if search(searchi+1,curri+1,currj,brd) != None:
                        return "Present"

                if currj != 0:
                    if search(searchi+1,curri,currj-1,brd) != None:
                        return "Present"

                if currj != rjindex:
                    if search(searchi+1,curri,currj+1,brd) != None:
                        return "Present"

                brd[curri][currj] = temp

            return None

        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if search(0,i,j,board) == "Present":
                    return True

        return False



        