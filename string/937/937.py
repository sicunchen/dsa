class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # if there's a tie, sort by identifier
        letters.sort(key=lambda log: log.split()[0])
        # if not sort by log body
        letters.sort(key=lambda log: log.split()[1:])

        return letters+digits
