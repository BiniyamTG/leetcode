class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        store=[]

        for i in range(len(word)):
            if word[i]==ch:
                store.append(i)
                m=min(store)
                l=word[0:m+1]
                l=l[::-1]
        