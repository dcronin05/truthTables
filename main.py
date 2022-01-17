from tabulate import tabulate
from rich import print


class TruthTable:

    def __init__(self, num_var):
        self.table = {}
        self.create_table(self, num_var)
        self.row_count = num_var

    @staticmethod
    def create_table(self, var_count, var_1='p', var_2='q', var_3='r', var_4='', var_5='', var_6=''):
        two_var_table = {var_1: ['T', 'T', 'F', 'F'],
                         var_2: ['T', 'F', 'T', 'F']}

        three_var_table = {var_1: ['T', 'T', 'T', 'T', 'F', 'F', 'F', 'F'],
                           var_2: ['T', 'T', 'F', 'F', 'T', 'T', 'F', 'F'],
                           var_3: ['T', 'F', 'T', 'F', 'T', 'F', 'T', 'F']}

        if var_count == 2:
            self.set_table(two_var_table)

        if var_count == 3:
            self.set_table(three_var_table)

    def add_column(self, header, equation):
        new_column = self.calculate(equation)

        self.table[header] = new_column

    def calculate(self, equation):
        new_column = []
        row = 0

        for i in range(pow(2, self.row_count)):
            p = True if self.table['p'][row] == 'T' else False
            q = True if self.table['q'][row] == 'T' else False
            try:
                r = True if self.table['r'][row] == 'T' else False
            except KeyError:
                pass
            new_column.append('T' if eval(equation) else 'F')
            row += 1

        return new_column

    def set_table(self, value):

        self.table = value

    def get_table(self):

        return self.table

    def disp_table(self):

        print(self.get_table())


def old_tables():
    table_1 = TruthTable(2)
    table_2 = TruthTable(3)
    table_3 = TruthTable(2)
    table_4 = TruthTable(3)

    table_1.add_column('not p and q', "not p and q")
    table_1.add_column('not (p and q)', "not (p and q)")
    print(tabulate(table_1.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_2.add_column('p or q', "p or q")
    table_2.add_column('r and p', "r and p")
    table_2.add_column('r and (p or q)', "r and (p or q)")
    table_2.add_column('(r and p) or q)', "(r and p) or q")
    print(tabulate(table_2.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_3.add_column('p ∨ q', "p or q")
    table_3.add_column('(¬p ∧ q) ∨ (p ∧ ¬q)', "(not p and q) or (p and not q)")

    print(tabulate(table_3.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_4.add_column('¬p ∧ q', "not p and q")
    table_4.add_column('¬p ∧ q ∧ r', "not p and q and r")
    print(tabulate(table_4.get_table(), headers='keys', tablefmt='github', showindex=False))

    table_5 = TruthTable(2)
    table_5.add_column('p → q', "False if p and q == False else True")
    table_5.add_column('¬p', "not p")
    table_5.add_column('¬p or q', "not p or q")
    print(tabulate(table_5.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    # (a)(¬p ∧ q) → p

    table_6 = TruthTable(2)
    table_6.add_column('(¬p ∧ q)', "(not p and q)")
    table_6.add_column('(¬p ∧ q) → p', "not (not p and q) or p")
    print(tabulate(table_6.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    # (b)(p → q) → (q → p)

    table_7 = TruthTable(2)
    table_7.add_column('(p → q)', "not p or q")
    table_7.add_column('(q → p)', "not q or p")
    table_7.add_column('(p → q) → (q → p)', "(not (not p or q)) or (not q or p)")
    print(tabulate(table_7.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()
    # (c)(p ∨ q) ↔ (q → ¬p)

    table_8 = TruthTable(2)
    table_8.add_column('(p ∨ q)', "p or q")
    table_8.add_column('(q → ¬p)', "not q or not p")
    table_8.add_column('(p ∨ q) ↔ (q → ¬p)', "(p or q) == (not q or not p)")
    print(tabulate(table_8.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    # (d)(p ↔ q) ⊕ (p ↔ ¬q)

    table_9 = TruthTable(2)
    table_9.add_column('(p ↔ q)', "p == q")
    table_9.add_column('(p ↔ ¬q)', "p == (not q)")
    table_9.add_column('(p ↔ q) ⊕ (p ↔ ¬q)', "(p == q) ^ (p == (not q))")
    print(tabulate(table_9.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    # (e)(p ∨ q) ↔ (q ∧ p)

    table_10 = TruthTable(2)
    table_10.add_column('(p ∨ q)', "p or q")
    table_10.add_column('(q ∧ p)', "q and p")
    table_10.add_column('(p ∨ q) ↔ (q ∧ p)', "(p or q) == (q and p)")
    print(tabulate(table_10.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    # ((s \land y) \to p) \land (p \to (s \land y))
    # p = p
    # s = q
    # y = r
    table_11 = TruthTable(3)
    table_11.add_column('q and r', "q and r")
    table_11.add_column('not (q and r) or p', "not (q and r) or p")
    table_11.add_column('not p or (q and r)', "not p or (q and r)")
    table_11.add_column('((q and r) to p) and (p to (q and r))', "(not(q and r) or p) and (not p or (q and r))")
    print(tabulate(table_11.get_table(), headers='keys', tablefmt='github', showindex=False))

    table_12 = TruthTable(2)
    table_12.add_column('r', "q")
    table_12.add_column('not r', "not q")
    print(tabulate(table_12.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_13 = TruthTable(2)
    table_13.add_column('not p and q', "not p and q")
    table_13.add_column('not q and p', "not q and p")
    table_13.add_column('p ^ q', "p ^ q")
    print(tabulate(table_13.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_14 = TruthTable(2)
    table_14.add_column('not (p and q)', "not (p and q)")
    table_14.add_column('not p and not q', "not p and not q")
    table_14.add_column('not p or not q', "not p or not q")
    print(tabulate(table_14.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_19 = TruthTable(2)
    table_19.add_column('p or q', "p or q")
    table_19.add_column('not q or p', "not p or q")
    table_19.add_column('(p or q) or (q to p)', "(p or q) or (not q or p)")
    print(tabulate(table_19.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_15 = TruthTable(2)
    table_15.add_column('(p to q)', "not p or q")
    table_15.add_column('p and not q', "p and not q")
    table_15.add_column('(p to q) == (p and not q)', "(not p or q) == (p and not q)")
    print(tabulate(table_15.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_16 = TruthTable(2)
    table_16.add_column('(p → q)', "not p or q")
    table_16.add_column('(p → q) ↔ p', "(not p or q) == p")
    print(tabulate(table_16.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_17 = TruthTable(2)
    table_17.add_column('(p → q)', "not p or q")
    table_17.add_column('(p → q) ∨ p', "(not p or q) or p")
    print(tabulate(table_17.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_17 = TruthTable(2)
    table_17.add_column('(¬p ∨ q)', "not p or q")
    table_17.add_column('(p ∧ ¬q)', "p and not q")
    table_17.add_column('(¬p ∨ q) ↔ (p ∧ ¬q)', "(not p or q) == (p and not q)")
    print(tabulate(table_17.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_18 = TruthTable(2)
    table_18.add_column('(¬p ∨ q)', "(not p) or q")
    table_18.add_column('(¬p ∧ q)', "(not p) and q")
    table_18.add_column('(¬p ∨ q) ↔ (¬p ∧ q)', "((not p) or q) == ((not p) and q)")
    print(tabulate(table_18.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_19 = TruthTable(2)
    table_19.add_column('p ↔ q', "p == q")
    table_19.add_column('(p → q) ∧ (q → p)', "(not p or q) and (not q or p)")
    table_19.add_column('p ↔ q and (p → q) ∧ (q → p)', "(p == q) == ((not p or q) and (not q or p))")
    print(tabulate(table_19.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_20 = TruthTable(2)
    table_20.add_column('¬(p ↔ q)', "not (p == q)")
    table_20.add_column('¬p ↔ q', "not p == q")
    table_20.add_column('¬(p ↔ q) and ¬p ↔ q', "(not (p == q)) == (not p == q)")
    print(tabulate(table_20.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_21 = TruthTable(2)
    table_21.add_column('¬p → q', "not (not p) or q")
    table_21.add_column('p ∨ q', "p or q")
    table_21.add_column('¬p → q and p ∨ q', "(not (not p) or q) == (p or q)")
    print(tabulate(table_21.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_22 = TruthTable(2)
    table_22.add_column('p → q', "not p or q")
    table_22.add_column('q → p', "not q or p")
    table_22.add_column('p → q and q → p', "(not p or q) == (not q or p)")
    print(tabulate(table_22.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_23 = TruthTable(2)
    table_23.add_column('¬p → q', "not (not p) or q")
    table_23.add_column('¬p ∨ q', "not p or q")
    table_23.add_column('¬p → q and ¬p ∨ q', "(not (not p)) == (not p or q)")
    print(tabulate(table_23.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_24 = TruthTable(3)
    table_24.add_column('(p → q) ∧ (r → q)', "(not p or q) and (not r or q)")
    table_24.add_column('(p ∧ r) → q', "(p and r) or q")
    table_24.add_column('(p → q) ∧ (r → q) and (p ∧ r) → q', "((not p or q) and (not r or q)) == ((p and r) or q)")
    print(tabulate(table_24.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_25 = TruthTable(3)
    table_25.add_column('p ∧ (p → q)', "p and (not p or q)")
    table_25.add_column('p ∨ q', "p or q")
    table_25.add_column('p ∧ (p → q) and p ∨ q', "(p and (not p or q)) == (p or q)")
    print(tabulate(table_25.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_26 = TruthTable(3)
    table_26.add_column('¬(p ∨ ¬q)', "(not (p or not q))")
    table_26.add_column('¬p ∧ q', "(not p and q)")
    table_26.add_column('¬(p ∨ ¬q) and ¬p ∧ q', "(not (p or not q)) == (not p and q)")
    print(tabulate(table_26.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_27 = TruthTable(2)
    table_27.add_column('¬(p ∨ ¬q)', "(not (p or not q))")
    table_27.add_column('¬p ∧ q', "(not p and q)")
    table_27.add_column('¬(p ∨ ¬q) and ¬p ∧ q', "(not (p or not q)) == (not p and q)")
    print(tabulate(table_27.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_28 = TruthTable(2)
    table_28.add_column('p ∧ (p → q)', "(p and (not p or q))")
    table_28.add_column('p → q', "(not p or q)")
    table_28.add_column('p ∧ (p → q) and p → q', "(not p or q) == (p and (not p or q))")
    print(tabulate(table_28.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_29 = TruthTable(2)
    table_29.add_column('p ∧ (p → q)', "(p and (not p or q))")
    table_29.add_column('p → q', "(not p or q)")
    table_29.add_column('p ∧ (p → q) and p → q', "(p and (not p or q)) == (not p or q)")
    print(tabulate(table_29.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_30 = TruthTable(2)
    table_30.add_column('p ∧ (p → q)', "(p and (not p or q))")
    table_30.add_column('p ∧ q', "(p and q)")
    table_30.add_column('p ∧ (p → q) and p ∧ q', "(p and (not p or q)) == (p and q)")
    print(tabulate(table_30.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_31 = TruthTable(3)
    table_31.add_column('not p to (q or not r)', "(not (not p) or (q or not r))")
    table_31.add_column('(r and not p) to q', "(not (r and not p) or q)")
    table_31.add_column('not p to (q or not r) == (r and not p) to q', "(not (not p) or (q or not r)) == (not (r and not p) or q)")
    print(tabulate(table_31.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_32 = TruthTable(3)
    table_32.add_column('((not p) to (q or not r))', "(not (not p) or (q or not r))")
    table_32.add_column('((r and not q) to p)', "(not (r and not q) or p)")
    table_32.add_column('((not p) to (q or not r)) == ((r and not q) to p)', "(not (not p) or (q or not r)) == (not (r and not q) or p)")
    print(tabulate(table_32.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_33 = TruthTable(2)
    table_33.add_column('((p) to (not q))', "(not p or (not q))")
    table_33.add_column('((not p) to q)', "((not (not p)) or q)")
    table_33.add_column('((p) to (not q)) == ((not p) to q)', "(not p or not q) == (not (not p) or q)")
    print(tabulate(table_33.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_34 = TruthTable(3)
    table_34.add_column('((r or not q) to p)', "((not (r or not q)) or p)")
    table_34.add_column('(p to (r and not q))', "((not p) or (r and not q))")
    table_34.add_column('((r or not q) to p) == (p to (r and not q))', "((not (r or not q)) or p) == ((not p) or (r and not q))")
    print(tabulate(table_34.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()


if __name__ == '__main__':

    table_35 = TruthTable(3)
    table_35.add_column('not (p and q) or r', "not (p and q) or r")
    table_35.add_column('not (p or q) or r', "not (p or q) or r")
    print(tabulate(table_35.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_36 = TruthTable(2)
    table_36.add_column('(p \\to q)', "(not p) or q")
    print(tabulate(table_36.get_table(), headers='keys', tablefmt='github', showindex=False))
    print()

    table_37 = TruthTable(2)
    table_37.add_column('(p \\to q)', "(not p) or q")
    table_37.add_column('not p', "(not p)")
    table_37.add_column('not q', "(not q)")
    print(tabulate(table_37.get_table(), headers='keys', tablefmt='latex', showindex=False))
    print()

    table_38 = TruthTable(3)
    table_38.add_column('(p or q)', "(p or q)")
    table_38.add_column('(q or r)', "(q or r)")
    table_38.add_column('(p or r)', "(p or r)")
    print(tabulate(table_38.get_table(), headers='keys', tablefmt='latex', showindex=False))
    print()

    # table_35 = TruthTable(3)
    # table_35.add_column('', "")
    # table_35.add_column('', "")
    # table_35.add_column('', "")
    # print(tabulate(table_35.get_table(), headers='keys', tablefmt='github', showindex=False))
    # print()

    # table_26 = TruthTable(3)
    # table_26.add_column('', "")
    # table_26.add_column('', "")
    # table_26.add_column('', "")
    # print(tabulate(table_26.get_table(), headers='keys', tablefmt='github', showindex=False))
    # print()

