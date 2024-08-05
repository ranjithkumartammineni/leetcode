#151. Reverse Words in a String
# Python 

class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        return ' '.join(l[::-1])
