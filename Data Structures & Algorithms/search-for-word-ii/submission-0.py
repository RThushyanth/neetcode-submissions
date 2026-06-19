class Solution(object):
    class TrieNode():
        def __init__(self):
            self.children = {}
            self.isend = False
            self.word = None

    def __init__(self):
        self.root = self.TrieNode()

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        for word in words:
            current = self.root
            for letter in word:
                try:
                    current.children[letter]
                except KeyError:
                    current.children[letter] = self.TrieNode()

                current = current.children[letter]
            
            current.isend = True
            current.word = word

        ans = []
        
        def triesearch(node,i,j):

            

            try:
                node.children[board[i][j]]
            except KeyError:
                return None
            else:
                next_node = node.children[board[i][j]]

                if next_node.isend == True:
                    ans.append(next_node.word)
                    next_node.isend = False

                temp = board[i][j]
                board[i][j] = 0
                if i != 0 and board[i-1][j] != 0:
                    triesearch(node.children[temp],i-1,j)
                if i != len(board)-1 and board[i+1][j] !=0:
                    triesearch(node.children[temp],i+1,j)
                if j != 0 and board[i][j-1] != 0:
                    triesearch(node.children[temp],i,j-1)
                if j != len(board[0])-1 and board[i][j+1] != 0:
                    triesearch(node.children[temp],i,j+1)
                board[i][j] = temp

                if not next_node.children:
                    del node.children[temp]

                return None

        current = self.root
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                triesearch(current,i,j)



        return ans