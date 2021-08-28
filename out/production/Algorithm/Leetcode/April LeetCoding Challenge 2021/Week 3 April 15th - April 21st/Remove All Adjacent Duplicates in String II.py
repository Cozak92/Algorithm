class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        for char in s:
            s = s.replace(char * k, "")  if char * k in s else s
                
        return s
            