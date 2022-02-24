class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        final_val = 0

        for op in operations:
            if '++' in op:
                final_val += 1
            else:
                final_val -= 1

        return final_val
