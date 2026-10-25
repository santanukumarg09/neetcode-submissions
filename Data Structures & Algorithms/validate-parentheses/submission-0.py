class Solution:
    def isValid(self, s: str) -> bool:
        
        stc = []

        open = ['(','[','{']
        close = [')',']','}']

        for br in s:
            if not stc and br in close:
                return False
                # break
                
            elif br in open:
                stc.append(br)

            elif (stc[-1] == open[0] and br == close[0]) or (stc[-1] == open[1] and br == close[1]) or (stc[-1] == open[2] and br == close[2]):
                stc.pop()

            else:
                return False
        return (not stc)

        


