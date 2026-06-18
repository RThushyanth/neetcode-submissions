class WordDictionary:
    class TrieNode():
        def __init__(self):
            self.children = {}
            self.isend = False

    def __init__(self):
        self.root = self.TrieNode()
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root
        for letter in word:
            try:
                current.children[letter]
            except KeyError:
                current.children[letter] = self.TrieNode()

            current = current.children[letter]
        
        current.isend = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(index, node):
            curr = node
            
            for i in range(index, len(word)):
                char = word[i]
                
                if char == '.':
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False 
                
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            
            return curr.isend
        
        return dfs(0, self.root)
        