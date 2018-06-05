class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res=[]
        i=0
        while i<len(words):
            size=0; begin=i
            while i<len(words):
                newsize=len(words[i]) if size==0 else size+len(words[i])+1
                if newsize<=maxWidth: size=newsize
                else: break
                i+=1
            spaceCount=maxWidth-size
            if i-begin-1>0 and i<len(words):
                everyCount=spaceCount/(i-begin-1)
                spaceCount%=i-begin-1
            else:
                everyCount=0
            j=begin
            while j<i:
                if j==begin: s=words[j]
                else:
                    s+=' '*(everyCount+1)
                    if spaceCount>0 and i<len(words):
                        s+=' '
                        spaceCount-=1
                    s+=words[j]
                j+=1
            s+=' '*spaceCount
            res.append(s)
        return res
print Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)