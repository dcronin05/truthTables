from IPython.display import display
import pandas as pd
from tabulate import tabulate

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    true = 'T'
    false = 'F'

    table = {'p': [true, true, true, true, false, false, false, false],
             'q': [true, true, false, false, true, true, false, false],
             'r': [true, false, true, false, true, false, true, false]
             }

    df = pd.DataFrame(table)

    print(tabulate(df, headers = 'keys', tablefmt='github', showindex=False))