import pandas as pd
from preprocesser import preprocessData
from sklearn import model_selection , naive_bayes , svm
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score

processedData = preprocessData()
# print( processedData )

dataset = pd.read_csv('dataset.csv',sep = ',')
# print(type(dataset))

train_x , test_x , train_y , test_y = model_selection.train_test_split(dataset['text'] ,dataset['label'] ,test_size = 0.3)
# print( train_x , test_x , train_y , test_y )

# y = [train_y[1] , test_y[1]]
encoder = LabelEncoder()
train_y = encoder.fit_transform(train_y)
test_y = encoder.fit_transform(test_y)
# print( train_y , test_y )

tfidf =  TfidfVectorizer( max_features = 5000 )
tfidf.fit(dataset['text'])
# print(tfidf)

train_x_tfidf = tfidf.transform(train_x)
test_x_tfidf = tfidf.transform(test_x)
# print( tfidf.vocabulary_ ,train_x_tfidf) 

naive = naive_bayes.MultinomialNB()
naive.fit(train_x_tfidf , train_y)

predictions = naive.predict(test_x_tfidf)
print( predictions )

score = accuracy_score(predictions , test_y)*100
print( "nv : " , score)


svm_classifier = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
svm_classifier.fit( train_x_tfidf , train_y )

predictions = svm_classifier.predict(test_x_tfidf)
print( predictions )

score = accuracy_score( predictions , test_y )*100
print("svm : ",score)