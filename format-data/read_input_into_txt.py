import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import os
outputpath_root = os.getcwd() + '\\'
def filter(string):

    stop_words = nltk.corpus.stopwords.words('english')
    word_tokens = word_tokenize(string)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    filtered_sentence = ''
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence = filtered_sentence + ' ' + w
    filtered_sentence_2 = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in filtered_sentence.split("\n")]
    return  filtered_sentence_2






def read_data():
    df = pd.read_csv('test.csv') #ten file chứa data nha
    #print(len(df))
    Text =df['Text'].tolist()
    ID =df['ID'].tolist()
    data =[]
    Text_list = []
    book_list_ID = []
    for data_text in Text:
        text_data_final = filter(data_text)
        text_data_final= str(text_data_final).lower()
        Text_list.append(text_data_final)

    for book_ID in ID:
        book_list_ID.append(book_ID)
    max_idx = len(book_list_ID)
    for i in range(0,max_idx):
        #data.append((book_list_ID[i], Text_list[i]))
        name_file = str(book_list_ID[i]) +".txt"
        outputpath = outputpath_root + name_file
        with open(outputpath,'a+') as file:
            tmp_text = Text_list[i]
            tmp_text = str(tmp_text)
            tmp_text = tmp_text.strip("['")
            tmp_text = tmp_text.strip("']")
            file.write(tmp_text)
            file.close()
    #print(data)


read_data()
# bien lua gia tri cuoi là "data" nha