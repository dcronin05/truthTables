from IPython.display import display
import pandas as pd
from tabulate import tabulate


class TruthTable:

    table = {}

    def __init__(self, var_count=2):
        self.create_table(var_count)

    def create_table(var_count, var_1='p', var_2='q', var_3='r', var_4='', var_5='', var_6=''):
        true = 'T'
        false = 'F'

        if var_count == 2:
            table = {var_1: [true, true, false, false],
                     var_2: [true, false, true, false]
                     }

        if var_count == 3:
            table = {var_1: [true, true, true, true, false, false, false, false],
                     var_2: [true, true, false, false, true, true, false, false],
                     var_3: [true, false, true, false, true, false, true, false]
                     }

        return pd.DataFrame(table)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(tabulate(TruthTable.create_table(3, 'p', 'q', 'r'), headers='keys', tablefmt='github', showindex=False))
    print(tabulate(TruthTable.create_table(2, 'p', 'q'), headers='keys', tablefmt='github', showindex=False))
