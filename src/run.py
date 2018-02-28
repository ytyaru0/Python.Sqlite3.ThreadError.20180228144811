import sqlite3
import threading

class CreateConnection(threading.Thread):
    connection = sqlite3.connect(':memory:')
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        sql = 'SELECT col1 from TEST_TABLE'
        self.connection.cursor().execute(sql)

if __name__ == '__main__':
    sql = "CREATE TABLE TEST_TABLE ( col1 INTEGER );"
    sqlite3.connect(':memory:').cursor().execute(sql)
    CreateConnection().start()
