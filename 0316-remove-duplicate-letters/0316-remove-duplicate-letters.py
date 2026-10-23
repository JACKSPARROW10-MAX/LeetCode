
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last = {ch: i for i, ch in enumerate(s)}

        for i, ch in enumerate(s):
            if ch in stack:
                continue

            while stack and stack[-1] > ch and last[stack[-1]] > i:
                stack.pop()

            stack.append(ch)

        return "".join(stack)
