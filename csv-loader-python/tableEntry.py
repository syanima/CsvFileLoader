import os

import pandas as pd
from sqlalchemy import create_engine

filePath = '/Users/syanima/practices/CsvFileLoader/csv-loader-python/mytable.csv'

def findTableName():
    file = os.path.basename(filePath)
    table = os.path.splitext(file)[0]
    return table

tableName = findTableName()


df = pd.read_csv(filePath)
df.columns = [c.lower() for c in df.columns]

engine = create_engine('postgresql://syanima:password@localhost:5432/filesystem')

df.to_sql(tableName, engine)
