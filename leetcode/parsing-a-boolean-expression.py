# parsing-a-boolean-expression.py
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        value_stack = []
        operator_stack = []
        for c in expression:
            if c == '' or c == '' or c == '' or c == '':
                operator_stack.append(c)
