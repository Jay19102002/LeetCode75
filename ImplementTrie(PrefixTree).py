# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
                
            cur = cur.children[c]

        cur.endOfWord = True

    def search(self, word: str) -> bool:
        temp = self.root
        for c in word:
            if c not in temp.children:
                return False
            temp = temp.children[c]
        return temp.endOfWord

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for c in prefix:
            if c not in temp.children:
                return False
            temp = temp.children[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# Example usage:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # Returns true
print(trie.search("app"))    # Returns false
print(trie.startsWith("app")) # Returns true
trie.insert("app")
print(trie.search("app"))    # Returns true
print(trie.startsWith("app")) # Returns true