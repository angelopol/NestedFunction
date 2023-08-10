from table import table
from center import center

def TableCenter(number):

    result = table(number)

    for TableResult in result:

        print(center(TableResult))