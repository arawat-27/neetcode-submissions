class Solution:
    def calPoints(self, operations: List[str]) -> int:
        newArr = []

        for op in operations:
            if op == "+":
                new = newArr[-1] + newArr[-2]
                newArr.append(new)
            elif op == "D":
                multiply = newArr[-1] * 2
                newArr.append(multiply)
            elif op == "C":
                newArr.pop()
            else:
                newArr.append(int(op))
        return sum(newArr)
        