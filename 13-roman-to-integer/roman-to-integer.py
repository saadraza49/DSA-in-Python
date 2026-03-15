class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }

        invalid_pairs = ["IL","IC","ID","IM","VX","VL","VC","VD",
                         "VM","XD","XM","LC","LD","LM","DM"]

        total = 0
        previous_val = 0

        # Check invalid subtractive pairs
        for j in range(len(s) - 1):
            pair = s[j] + s[j+1]
            if pair in invalid_pairs:
                raise ValueError(f"Invalid Roman numeral pair: {pair}")

        # Count consecutive letters
        count = 1
        prev = ""
        for ch in s:
            if ch not in roman:
                raise ValueError(f"Invalid Roman numeral: {ch}")
            if ch == prev:
                count += 1
                if ch in ["V", "L", "D"] and count > 1:
                    raise ValueError(f"{ch} cannot be repeated")
                if ch in ["I", "X", "C", "M"] and count > 3:
                    raise ValueError(f"{ch} cannot be repeated more than 3 times")
            else:
                count = 1
            prev = ch

        # Convert Roman to integer
        for ch in reversed(s):
            current_val = roman[ch]
            if current_val >= previous_val:
                total += current_val
            else:
                total -= current_val
            previous_val = current_val

        return total