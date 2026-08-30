class Solution:
    def longestPalindrome(self, s: str):
        # Values passed in are in index values from the loop
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1: r]

        result = ""
        # Run a loop
        # Match the length of the values returned from expand and result
        # If the returned values from expland is greater than expand. We reset the value of result to be expands
        
        for i in range(len(s)):
            sub1 = expand(i, i)
            if len(sub1) > len(result):
                result = sub1

            sub2 = expand(i, i+1)
            if len(sub2) > len(result):
                result = sub2
        print(result)
        return result

def main():
    solution = Solution()
    solution.longestPalindrome("abcba")

main()