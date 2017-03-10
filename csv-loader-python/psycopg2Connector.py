import os

import psycopg2
from psycopg2.extensions import AsIs


def findTableName():
    filePath = '/Users/syanima/practices/csv-loader-python/test12.csv'
    file = os.path.basename(filePath)
    table = os.path.splitext(file)[0]
    return table

tableName = findTableName()

try:
    conn = psycopg2.connect("dbname='filesystem' user='syanima' host='localhost' password=''")
    print "I am able to connect to the database"
except:
    print "I am unable to connect to the database"

cur = conn.cursor()

try:

    cur.execute("Create table  %(table)s (content varchar,content2 varchar,content3 varchar);",{"table": AsIs(tableName)})
    f = open('/Users/syanima/practices/csv-loader-python/test12.csv', 'r')
    cur.copy_from(f,tableName,sep=',')
    f.close()
    conn.commit()
    cur.close()
    conn.close()
except:
    print "I can't execute the query"

