from utils import *
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def count_num(s):
            code_book = [0]*26
            for i in s:
                code_book[ord(i)-ord('a')] += 1
            code_book = [str(i) for i in code_book]
            return '/'.join(code_book)
        hash_dict = {}
        for s in strs:
            hash_code = count_num(s)
            if hash_code not in hash_dict.keys():
                hash_dict[hash_code] = [s]
            else:
                hash_dict[hash_code].append(s)
        res = []
        for i in hash_dict.keys():
            res.append(hash_dict[i])
        return res
    
s = Solution()
strs = ["bdddddddddd","bbbbbbbbbbc"]
print(s.groupAnagrams(strs))