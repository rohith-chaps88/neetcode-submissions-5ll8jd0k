from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        store = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                store.append(int(token))
                continue

            right = store.pop()
            left = store.pop()

            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            else:
                result = int(left / right)

            store.append(result)

        return store[0]

