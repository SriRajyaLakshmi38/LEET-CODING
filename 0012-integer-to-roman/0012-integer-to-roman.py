class Solution:
    def intToRoman(self, num: int) -> str:
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        units = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        th = num // 1000
        h = (num % 1000) // 100
        t = (num % 100) // 10
        u = num % 10

        result = thousands[th] + hundreds[h] + tens[t] + units[u]
        return result