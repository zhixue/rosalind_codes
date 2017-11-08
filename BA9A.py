class TrieNode(object):
    def __init__(self,fp=0,pos=1,c=None,word=None):
        self.children = []
        self.fp = fp
        self.pos = pos
        self.c = c


class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        self.maxpos = 1
        self.nodelist = []

    def add(self, s):
        """Add a string to this trie."""
        p = self.root
        n = len(s)
        if self.maxpos == 1:#first word
            for i in range(n):
                self.maxpos += 1
                new_node = TrieNode(fp=p.pos, pos=self.maxpos, c=s[i],word = s[:i])
                self.nodelist.append(new_node)
                p.children.append(new_node)
                p = new_node
        else:#other word
            for i in range(n):
                if s[i] not in [node.c for node in p.children]:
                    self.maxpos += 1
                    new_node = TrieNode(fp=p.pos, pos=self.maxpos, c=s[i])
                    self.nodelist.append(new_node)
                    p.children.append(new_node)
                    p = new_node
                else:
                    for node in p.children:#find the fathernode
                        if s[i] == node.c:
                            p = node

    def addlist(self,wordlists):
        for word in wordlists:
            self.add(word)



    def show(self):
        """Judge where s is in this trie."""
        for one in self.nodelist:
            print(str(one.fp-1)+'->'+str(one.pos-1)+':'+one.c)


if __name__ == '__main__':
    trie = Trie()
    listbox = []
    for line in open('rosalind_ba9a.txt'):
        listbox.append(line.rstrip())
    trie.addlist(listbox)
    trie.show()