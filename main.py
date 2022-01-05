from IPython.display import display
import pandas as pd
from tabulate import tabulate


class TruthTable:

    def __init__(self, num_var):
        self.table = {}
        self.create_table(self, num_var)

    @staticmethod
    def create_table(self, var_count, var_1='p', var_2='q', var_3='r', var_4='', var_5='', var_6=''):
        true = 'T'
        false = 'F'

        two_var_table = {var_1: [true, true, false, false],
                         var_2: [true, false, true, false]}

        three_var_table = {var_1: [true, true, true, true, false, false, false, false],
                           var_2: [true, true, false, false, true, true, false, false],
                           var_3: [true, true, true, true, false, false, false, false]}

        if var_count == 2:
            self.set_table(two_var_table)

        if var_count == 3:
            self.set_table(three_var_table)

    def add_column(self, header, equation):


    def set_table(self, value):
        self.table = value

    def get_table(self):
        return self.get_table()

    def disp_table(self):
        print(self.get_table())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    table_1 = TruthTable(2)
    table_2 = TruthTable(3)

    print(tabulate(table_1.get_table(), headers='keys', tablefmt='github', showindex=False))

    print()

    print(tabulate(table_2.get_table(), headers='keys', tablefmt='github', showindex=False))
