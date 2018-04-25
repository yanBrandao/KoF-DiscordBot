import psycopg2

class DBConnection(object):
    _db=None
    
    def __init__(self):
       self._db = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='',port='5433')

    def changeDatabase(self, sql):
        returnBool = True
        try:
            dbCursor=self._db.cursor()
            dbCursor.execute(sql)
            dbCursor.close()
            self._db.commit()
        except Exception as e:
            print(e)
            returnBool = False
        return returnBool

    def checkDatabase(self, sql):
        result=None
        try:
            dbCursor=self._db.cursor()
            dbCursor.execute(sql)
            result=dbCursor.fetchall()
        except:
            return None
        return result

    def close(self):
        self._db.close()