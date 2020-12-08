puzzle_input = open('day1.txt', 'r').read().split('\n')

def fix_report(report):
    for expense1 in report:
        for expense2 in report:
            for expense3 in report:
                expense1 = int(expense1)
                expense2 = int(expense2)
                expense3 = int(expense3)
                if expense1 + expense2 + expense3 == 2020:
                    return expense1 * expense2 * expense3

print(fix_report(puzzle_input))
