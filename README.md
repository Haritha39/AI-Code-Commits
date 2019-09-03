# AI-Code-Commits
Extracting AI commits on git repositories


## Goal
Separate the commits as ai commits and non-ai commits

## Flow

Webhook 
 \
 |\
API
  \
 |\
gitOps<------->classification
\
 |\
Mysql

### Steps

1. Start the project by running init.py 

    ```python3 init.py >> output.csv```
2. Entire project will be cloned using information came in webhook
3. Checked out to the branch mentioned in webhook data.
4. Read each and every file by walking through every sub directories and directories.
5. This entire data will send to preprocessing.
6. During Preprocessing , the data will be cleaned by removing stop words , lemmatization etc.
7. The important step in Preprocessing is , as our input data is only code - i took out the important keywords like libraries , modules names , packages etc by data cleaning .
8. Took out the keywords which are not in actual dictionary , because they are simple english words .
9. I created a machine learning (ai) corpus out of data i collected from one of the github repository :
    https://github.com/josephmisiti/awesome-machine-learning#apl
10. I have checked if there is any matching of our data with the corpus .
11. If matched , i considered it as AI commit,that's how the idea works

