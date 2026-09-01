# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.

# Conversion: Read the integer by skipping leading zeros until a non-digit character 
# is encountered or the end of the string is reached. If no digits were read, then the result is 0.

# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], 
# then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, 
# and integers greater than 231 - 1 should be rounded to 231 - 1.

# Return the integer as the final result.
class Solution:
    def myAtoi(self, s: str) -> int:
        pos = 0
        s_len = len(s)
        sign = 1
        operations = ["+", "-"]
        value = 0

        # Below variables help to break out of the loop for cases such as
        # "   0 123"
        # "  + = 340"
        # "  =-2  "
        # Breaks if the next character after locating an operator sign a white space or another operator sign
        # Breaks if a digit is located but is followed by white space or operator sign
        first_digit_locked = False
        first_symbol_locked = False

        while pos < s_len:
            current_char = s[pos]


            # If not a digit. Check for possible that can break the loop
            if not current_char.isdigit():
                
                # Ok to continue ONLY IF first few indexes are white spaces
                if current_char == " " and first_digit_locked != True and first_symbol_locked != True:
                    value = value + 0

                # Will assign negative(-) or positive(+) value if first character '-' or '+' after white spaces
                # Once set if another symbol is followed up then break the loop
                # If a digit is set and followed by a symbol then break the loop
                elif current_char in operations:
                    if not first_digit_locked and not first_symbol_locked:
                        sign = 1 if current_char == "+" else -1
                        first_symbol_locked =True
                    else:
                        break

                # Break for safety reasons...I think
                # Forgot why I decided to add this but it resolves other cases
                else:   
                    break

            # string together all sequential digits
            elif current_char.isdigit() :
                first_digit_locked = True
                value = (value * 10) + int(current_char)

                    
            pos += 1

        # account for "+" or "-" operators located
        value = sign * value
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)
        return value



def main():
    solution = Solution()
    solution.myAtoi("  +0 2")

main()