class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            #create array of size 26 for each letter in alphabet
            #initially 0 
            count = [0] * 26
            #count the frequenceis by getting the current characters ascii value - 'a' ascii value
            for c in string:
                count[ord(c) - ord('a')] += 1
            #append word to key that matches its letter count
            res[tuple(count)].append(string)
        return list(res.values())