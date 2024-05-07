import sqlite3

def saveDataIntoSQLite(valuesToInsert:tuple):
    connection = sqlite3.connect("imgDetection.db")
    cursor = connection.cursor()
    QUERY_INSERT = """INSERT INTO 'MODELO.ImageDetectionLogs' (firmasDetectadas, modelResult, confidenceBySign, nameImage)
                   VALUES (?,?,?,?);
                   """
    cursor.execute(QUERY_INSERT,valuesToInsert)
    connection.commit()
    cursor.close()
    connection.close()
    return {"status":200}