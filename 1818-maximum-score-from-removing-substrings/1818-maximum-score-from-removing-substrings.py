class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pair(s, first, second, points):
            stack = []
            gain = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    gain += points
                else:
                    stack.append(char)
            return ''.join(stack), gain

        # Decide which to remove first: 'ab' or 'ba'
        if x >= y:
            s, gain1 = remove_pair(s, 'a', 'b', x)
            _, gain2 = remove_pair(s, 'b', 'a', y)
        else:
            s, gain1 = remove_pair(s, 'b', 'a', y)
            _, gain2 = remove_pair(s, 'a', 'b', x)

        return gain1 + gain2
