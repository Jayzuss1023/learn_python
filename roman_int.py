# Given a roman numeral, convert it to an integer.
roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            
            curr = roman[s[i]]
            next_val = roman[s[i+1]] if i+1 < len(s) else 0
            if curr < next_val:
                result -= curr
            else:
                result += curr
        print(result)

def main():
    romantoint = Solution()
    romantoint.romanToInt("MCMXCIV")

main()