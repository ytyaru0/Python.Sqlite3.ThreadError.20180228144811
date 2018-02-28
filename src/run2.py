import dataset
#import sqlite3
import threading

class CreateConnection(threading.Thread):
    #connection = dataset.connect('sqlite://', **{'check_same_thread': False})
    connection = dataset.connect('sqlite://', engine_kwargs={'check_same_thread': False})
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        sql = 'SELECT col1 from TEST_TABLE'
        self.connection.query(sql)

if __name__ == '__main__':
    sql = "CREATE TABLE TEST_TABLE ( col1 INTEGER );"
    dataset.connect('sqlite://', engine_kwargs={'check_same_thread': False}).query(sql)
    #CreateConnection().start()
    th = CreateConnection()
    th.start()
    #th.join()
    print('完了！')

