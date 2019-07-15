# --------------------------------------------------------------------------------------------------
# SQLite3 ソリューション
# --------------------------------------------------------------------------------------------------

import sqlite3

class SqLite3Adapter:

    def __init__(self):
        self.myConnection = None

    def createDB(self, xml):
        pass

    def openDB(self, dbName):
        self.myConnection = sqlite3.connect(database = dbName)

    def executeSql(self, sql, params = None):
        if (params == None):
            self.myConnection.execute(sql)
        else:
            self.myConnection.execute(sql, params)

    def getCursor(self, sql, params = None):
        myCursor = self.myConnection.cursor()
        if (params == None):
            response = myCursor.execute(sql)
        else:
            response = myCursor.execute(sql, params)
        
        return response
    
    def getRows(self, sql, params = None):
        rows = self.getCursor(sql, params)
        for row in rows.fetchall():
            yield row
    
    def getRow(self, sql, params = None):
        return self.getCursor(sql, params).fetchone()

    def commitDB(self):
        self.myConnection.commit()
    
    def rollbackDB(self):
        self.myConnection.rollback()
    
    def closeDB(self):
        self.myConnection.close()