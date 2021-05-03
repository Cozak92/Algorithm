class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", 
        '8':"tuv", '9':"wxyz"}
    
        cmb = [''] if digits else []
        
        for l in digits:
            cmb = [p + q for p in cmb for q in dict[l]]
        
        return cmb
            


    # class Solution(object):
    # def letterCombinations(self, digits):
    #     """
    #     :type digits: str
    #     :rtype: List[str]
    #     """
    #     interpret_digit = {
    #         '1': '',
    #         '2': 'abc',
    #         '3': 'def',
    #         '4': 'ghi',
    #         '5': 'jkl',
    #         '6': 'mno',
    #         '7': 'pqrs',
    #         '8': 'tuv',
    #         '9': 'wxyz',
    #         '0': ' '}
    #     all_combinations = [''] if digits else []
    #     for digit in digits:
    #         current_combinations = list()
    #         for letter in interpret_digit[digit]:
    #             for combination in all_combinations:
    #                 current_combinations.append(combination + letter)
    #         all_combinations = current_combinations
    #     return all_combinations