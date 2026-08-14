from collections import defaultdict
from typing import List


class Solution():
    def group_anagram(self, strs=List[str]):
        anagram_list=defaultdict(list)
        result=[]

        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_list[sorted_s].append(s)

        for value in anagram_list.values():
            result.append(value)

        print(result)



def main():
    anagram=["eat", "tea", "tan", "ate", "nat", "bat"]
    solution=Solution()
    solution.group_anagram(anagram)

main()