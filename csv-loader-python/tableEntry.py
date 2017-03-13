import os

import pandas as pd
from sqlalchemy import create_engine

filePath = './mytable100.csv'

def findTableName():
    file = os.path.basename(filePath)
    table = os.path.splitext(file)[0]
    return table

tableName = findTableName()


df = pd.read_csv(filePath)
print df
df.columns = [c.lower() for c in df.columns]

engine = create_engine('postgresql://syanima:password@localhost:5432/filesystem')

df.to_sql(tableName, engine)
