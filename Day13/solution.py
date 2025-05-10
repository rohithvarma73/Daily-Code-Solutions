class Solution:
    def intToRoman(self, num: int) -> str:
        # Map of Roman numerals in descending order of value
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman = ""
        i = 0
        
        while num > 0:
            # Find how many times the current value fits in num
            count = num // val[i]
            # Append the corresponding symbol that many times
            roman += syms[i] * count
            # Reduce num accordingly
            num -= val[i] * count
            # Move to the next symbol
            i += 1
        
        return roman
