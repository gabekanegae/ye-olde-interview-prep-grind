class TrieNode:
    def __init__(self, val, end=False):
        self.val = val
        self.children = dict()
        self.end = end

class Trie:
    def __init__(self):
        self.root = TrieNode(".")

    def insert(self, word):
        p = self.root
        c = 0

        while c < len(word):
            if word[c] not in p.children:
                p.children[word[c]] = TrieNode(word[c])
            p = p.children[word[c]]
            c += 1

        p.end = True

    def search(self, word):
        p = self.root
        c = 0

        while c < len(word) and word[c] in p.children:
            p = p.children[word[c]]
            c += 1

        return (c == len(word) and p.end)

    def startsWith(self, prefix):
        p = self.root
        c = 0

        while c < len(prefix) and prefix[c] in p.children:
            p = p.children[prefix[c]]
            c += 1

        return c == len(prefix)

trie = Trie()

trie.insert("apple")
trie.insert("apples")
print(trie.search("apple")) # True
print(trie.search("app")) # False
print(trie.startsWith("app")) # True
trie.insert("app")
print(trie.search("app")) # True