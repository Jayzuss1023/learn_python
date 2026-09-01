class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        mat = [[] for _ in range(numRows)]
        i = 0
        n = len(s)

        # Loop through each letter. Run a check on where to append
        # Loop through each mat and append letter
        while i < n:
            # Down operation. Starts at mat[0] and works its way down. i is incremented
            # 0: []
            # 1: []
            # 2: []
            # 3: []
            # 4: []
            # Operation stops when i == n
            # Queue next for statement below
            for down in range(numRows):
                if i < n:
                    mat[down].append(s[i])
                    i += 1

            # Standard Count [1, 2, 3, 4, 5]
            # Python Count   [0, 1, 2, 3, 4]
            # Subtract 2 from standard count you're left with 3
            # We'll now append to Python's index[3] and accumulate till we stop at index[0]
            # Queue above from loop
            for up in range(numRows - 2, 0, -1):
                if i < n:
                    mat[up].append(s[i])
                    i += 1

        ans = ""
        for row in mat:
            print("ROW : ", row)
            ans += ''.join(row)
        return ans

def main():
    solution = Solution()
    solution.convert("HELLOWORLD", 5)
    
main()