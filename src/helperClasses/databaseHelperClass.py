import pymysql
from helperClasses.constantClass import databaseConstants

class databaseHelper(databaseConstants):

    def __init__( self , db_config ,logger ):
        self.logger = logger
        self.config = db_config
        self.logger.info(" This is a constructor ")
        self.connectDatabase()

    def connectDatabase(self):        
        try:
            dbConnection = pymysql.connect( host = self.config["host"],port = self.config["port"], \
                                            user = self.config["root"],\
                                            password = self.config["passwd"], db = self.config["database"] )
            self.logger.info("Successfully Connected to Mysql Database")
            self.cursor = dbConnection.cursor()            
        except Exception as error :
            self.logger.error("mysql.py - Error in connecting to mysql :: {}".format(error) )
        return

    def createCommitTable( self ):

        tableName = databaseConstants.table_ai_commit
        tableDesc = databaseConstants.table_ai_commit_pid + " int," \
                    +databaseConstants.table_ai_commit_commits + " int," \
                    + databaseConstants.table_ai_commit_time + " datetime," \
                    + databaseConstants.table_ai_commit_cid + " char(64) ,"\
                    + databaseConstants.table_ai_commit_ai + " char(16) ,"\
                    + databaseConstants.table_ai_commit_lang + " char(64) ,"\
        
        try:
            self.cursor.execute( "CREATE TABLE IF NOT EXISTS "+ tableName + "("+ tableDesc + ")" )
            
            self.logger.info( " Table is created : {}".format(tableName) )
        except Exception as error:
            self.logger.error("databaseHelperClass.py - Error in createCommitTable method :: {}".format(error) )

    def selectCommitTable( self , values ):
        
        tableName = databaseConstants.table_ai_commit
        condition = databaseConstants.table_ai_commit_cid
        try:
            if( values is not None ):
                result = self.cursor.execute("SELECT * FROM " + tableName + " WHERE " + condition +"=%s" , (values) )     
            else:
                result = self.cursor.execute( "SELECT *  FROM " + tableName )     
            self.logger.info( " Data  is retireived from : {}".format(tableName) )
            return result
        except Exception as error:
            self.logger.error("databaseHelperClass.py - Error in selectCommitTable method :: {}".format(error) )
            return False

    def insertIntoCommitTable( self , values ):
        tableName = databaseConstants.table_ai_commit
        tableDesc = "("+databaseConstants.table_ai_commit_pid + "," \
                       +databaseConstants.table_ai_commit_commits + "," \
                       +databaseConstants.table_ai_commit_time + "," \
                       +databaseConstants.table_ai_commit_cid + ","\
                       + databaseConstants.table_ai_commit_ai + ","\
                       + databaseConstants.table_ai_commit_lang + ") " 
        formatString = "(%s,%s,%s,%s,%s,%s)"

        try:   
            insert = self.cursor.execute("INSERT INTO "+ tableName + tableDesc + " VALUES " + formatString , values )     
            self.logger.info( " Data  is inserted into : {}".format(tableName) )
        except Exception as error:
            self.logger.error("databaseHelperClass.py - Error in insertIntoCommitTable method :: {}".format(error) )
