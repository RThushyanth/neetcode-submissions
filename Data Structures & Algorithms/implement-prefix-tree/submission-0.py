class PrefixTree:
    class TrieNode():
        def __init__(self):
            self.children = {}
            self.isend = False

    def __init__(self):
        self.root = self.TrieNode()
        

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            try:
                current.children[letter]
            except KeyError:
                current.children[letter] = self.TrieNode()

            current = current.children[letter]
        
        current.isend = True


    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            try:
                current.children[letter]
            except KeyError:
                return False
            else:
                current = current.children[letter]

        if current.isend:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for letter in prefix:
            try:
                current.children[letter]
            except KeyError:
                return False
            else:
                current = current.children[letter]
        
        return True
        
        