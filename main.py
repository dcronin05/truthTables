from tabulate import tabulate


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


if __name__ == '__main__':

    table_1 = TruthTable(2)
    table_2 = TruthTable(3)
    table_3 = TruthTable(2)

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
    