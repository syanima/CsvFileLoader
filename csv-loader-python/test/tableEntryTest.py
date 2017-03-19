import unittest
from src.tableEntry import *


class TestDataBaseEntry(unittest.TestCase):
    def setUp(self):
        self.username = "syanima"
        self.password = "password"
        self.fileName = "mycsv.csv"

    def test_table_name(self):
        copyToDatabase()
        self.assertEqual("mycsv",findTableName())


if __name__ == '__main__':
    unittest.main()