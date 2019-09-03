import json

def checkCommit( data ):
    dataset = open("scientificKeywords.txt","r")
    dataset = dataset.read()
    dataset = json.loads( dataset )

    keys = dataset.keys()
    values = dataset.values()

    print( type( dataset ))

    langCount = {}

    for each in data:
        for eachKey in keys:
            if( each in dataset[eachKey]):
                if( each in langCount.keys() ):
                    langCount[each] = langCount[each] + 1
                else:
                    langCount[each] = 1
            
            
    return langCount