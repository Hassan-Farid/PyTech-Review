#Simplest model for text to numerical vector conversion

'''
Psuedocode:
1. Find unique words from a set of words and sentences.
2. Count the number of occurences of each unqiue word for each element in given set.
3. If the unique word is present represent by 1 otherwise 0.
'''

#Disadvantage of this approach is that complexity increases with respect to increase in number of unqiue words.

from sklearn.feature_extraction.text import CountVectorizer

#Consider the set of following sentences
text_list = ["I like Soccer", "Soccer is my favourite sports", "He is going to the market", "He bought many things from the market"]

#Using Bag_of_Words Model on given set of texts
vectorizer = CountVectorizer(binary=True)
vectors = vectorizer.fit_transform(text_list)

#Displaying the unqiue text words
print(vectorizer.get_feature_names())

#Displaying the numerical vectors obtained
print(vectors.toarray())

#Creating a classifier using Bag of Words that seperates statements of Soccer from that of Market
class Category:
    SOCCER = "SOCCER"
    MARKET = "MARKET"
    
#Classifying given text into categories
text_category = [Category.SOCCER, Category.SOCCER, Category.MARKET, Category.MARKET]

#Creating the classifier
from sklearn import svm

svm_classifier = svm.SVC(kernel="linear")
svm_classifier.fit(vectors, text_category)

#Checking for other statements via classifier
sample1 = vectorizer.transform(["they were playing soccer"])

print("Sample 1 belongs to {}".format(svm_classifier.predict(sample1)))
