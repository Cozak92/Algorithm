class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        prev = "-1"
        group = []
        for num in s:
            if num != prev:
                group.append(1)
            else:
                group[-1] += 1
            prev = num
        
        answer = 0

        for i in range(len(group)-1):

            answer += min(group[i],group[i+1])

        
        return answer
            




