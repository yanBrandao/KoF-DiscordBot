import psycopg2

class DBConnection(object):
    _db=None
    
    def __init__(self):
        file = open('host.token', 'r')
        filedbname = open('dbname.token', 'r')
        fileuser = open('user.token', 'r')
        filepass = open('pass.token', 'r')
        tokenHOST = file.read()
        tokenDATA = filedbname.read()
        tokenUSER = fileuser.read()
        tokenPASS = filepass.read()
        
        self._db = psycopg2.connect(host=tokenHOST, database=tokenDATA, user=tokenUSER, password=tokenPASS,port='5432')

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