import cloneProject
import checkoutBranch
import readEveryFile 
from classificationModel import  preprocesser
from classificationModel import model

def aiCodeCommit( request_data , connectDB , logger , config ):

    try:
        cloneProject.cloning( config["git"] , request_data )
        checkoutBranch.checkout_branch( config["git"],request_data , logger )
        raw_data = readEveryFile.read_file( config["git"],request_data , logger )
        processedDataList = preprocesser.preprocessData( raw_data )
        finalData = model.checkCommit( processedDataList )

        commitId = request_data["commits"][-1]["id"]
        project_id = request_data["project"]["id"]
        commitCount = request_data["total_commits_count"]
        timestamp = request_data["commits"][-1]["timestamp"]

        if( finalData is not None ):
            
            lang = ",".join( eachKey for eachKey in finalData.keys() )
            ai = "True"
            connectDB.insertIntoCommitTable((project_id,commitCount,timestamp,commitId,lang,ai))
            print( commitId , "True")
        else:
            connectDB.insertIntoCommitTable((project_id,commitCount,timestamp,commitId,"None","False"))
            print( commitId , "False")

    except Exception as error:
        logger.error("gitOperations.steps.py - {}".format(error))