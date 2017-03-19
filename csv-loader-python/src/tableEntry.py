import os

import pandas as pd
from sqlalchemy import create_engine


userName = raw_input('Enter postgres user name :')
password = raw_input('Enter postgres password :')
fileName = raw_input('Enter csv file name :')

filePath = '~/Downloads/' + fileName

def findTableName():
    file = os.path.basename(filePath)
    table = os.path.splitext(file)[0]
    table = table.translate(None, '()" "')
    return table


def copyToDatabase():

    df = pd.read_csv(filePath)
    df.columns = [c.lower() for c in df.columns]

    engine = create_engine('postgresql://' + userName + ':' + password +'@localhost:5432/filesystem')

    df.to_sql(findTableName(), engine)

copyToDatabase()